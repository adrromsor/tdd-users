from http.client import CREATED, OK

from fastapi import APIRouter, Depends

from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.application.search_users.search_users_query_handler import SearchUsersQueryHandler
from src.delivery.api.v1.users.users_requests import UserCreateRequest
from src.delivery.api.v1.users.users_responses import UserResponse, UsersResponse
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository

users_router = APIRouter()
user_repository = InMemoryUserRepository()


def get_create_user_command_handler() -> CreateUserCommandHandler:
    return CreateUserCommandHandler(user_repository)


def get_search_users_query_handler() -> SearchUsersQueryHandler:
    return SearchUsersQueryHandler(user_repository)


@users_router.put("/users", status_code=CREATED)
def create_user(
    request: UserCreateRequest,
    handler: CreateUserCommandHandler = Depends(get_create_user_command_handler),
) -> None:
    command = CreateUserCommand(id=request.id, name=request.name, age=request.age)
    handler.execute(command)


@users_router.get("/users", status_code=OK)
def search_users(handler: SearchUsersQueryHandler = Depends(get_search_users_query_handler)) -> UsersResponse:
    response = handler.execute()
    users = [
        UserResponse(id=user_primitives["id"], name=user_primitives["name"], age=user_primitives["age"])
        for user_primitives in response.users
    ]
    return UsersResponse(users=users)

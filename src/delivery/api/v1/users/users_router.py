from http.client import CREATED, NOT_FOUND, OK

from fastapi import APIRouter, Depends, HTTPException

from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.application.find_user.find_user_query import FindUserQuery
from src.application.find_user.find_user_query_handler import FindUserQueryHandler
from src.application.search_users.search_users_query_handler import SearchUsersQueryHandler
from src.delivery.api.v1.users.users_requests import UserCreateRequest
from src.delivery.api.v1.users.users_responses import UserResponse, UsersResponse
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository

users_router = APIRouter()
user_repository = InMemoryUserRepository()


def get_create_user_command_handler() -> CreateUserCommandHandler:
    return CreateUserCommandHandler(user_repository)


def get_find_user_query_handler() -> FindUserQueryHandler:
    return FindUserQueryHandler(user_repository)


def get_search_users_query_handler() -> SearchUsersQueryHandler:
    return SearchUsersQueryHandler(user_repository)


@users_router.put("/users/{user_id}", status_code=CREATED)
def create_user(
    user_id: str,
    request: UserCreateRequest,
    handler: CreateUserCommandHandler = Depends(get_create_user_command_handler),
) -> None:
    command = CreateUserCommand(id=user_id, name=request.name, age=request.age)
    handler.execute(command)


@users_router.get("/users/{user_id}", status_code=OK)
def find_user(user_id: str, handler: FindUserQueryHandler = Depends(get_find_user_query_handler)) -> UserResponse:
    query = FindUserQuery(id=user_id)
    response = handler.execute(query)
    if response is None:
        raise HTTPException(status_code=NOT_FOUND, detail="User not found")

    return UserResponse(
        id=response.id,
        name=response.name,
        age=response.age,
    )


@users_router.get("/users", status_code=OK)
def search_users(handler: SearchUsersQueryHandler = Depends(get_search_users_query_handler)) -> UsersResponse:
    response = handler.execute()
    users = [
        UserResponse(id=user_primitives["id"], name=user_primitives["name"], age=user_primitives["age"])
        for user_primitives in response.users
    ]
    return UsersResponse(users=users)

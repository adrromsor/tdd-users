from http.client import CREATED
from fastapi import APIRouter, Depends

from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.delivery.api.v1.users.users_requests import UserCreateRequest

users_router = APIRouter()


def get_create_user_command_handler() -> CreateUserCommandHandler:
    return CreateUserCommandHandler()


@users_router.post("/users", status_code=CREATED)
def create_user(
    request: UserCreateRequest,
    handler: CreateUserCommandHandler = Depends(get_create_user_command_handler),
) -> None:
    command = CreateUserCommand(name=request.name, age=request.age)
    handler.execute(command)

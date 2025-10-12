from unittest.mock import Mock

from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository


class TestCreateUserCommandHandler:
    def test_create_user_command_handler_saves_user(self) -> None:
        command = CreateUserCommand(id="4a079c0b-5474-4648-a836-8cc7c4e4ff3d", name="Mike", age=27)
        repository = Mock(spec=InMemoryUserRepository)
        handler = CreateUserCommandHandler(repository)

        handler.execute(command)

        expected_user = User.create(command.id, command.name, command.age)
        repository.save.assert_called_once_with(expected_user)

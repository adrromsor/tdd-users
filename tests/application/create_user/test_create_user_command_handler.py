from unittest.mock import Mock

from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository


class TestCreateUserCommandHandler:
    def test_create_user_command_handler_saves_user(self) -> None:
        command = CreateUserCommand(id="123", name="Mike", age=27)
        repository = Mock(spec=InMemoryUserRepository)
        handler = CreateUserCommandHandler(repository)

        handler.execute(command)

        expected_user = User(id="123", name="Mike", age=27)
        repository.save.assert_called_once_with(expected_user)

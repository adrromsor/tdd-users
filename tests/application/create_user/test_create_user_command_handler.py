from unittest.mock import Mock

from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository
from tests.domain.user_primitives_mother import UserPrimitivesMother


class TestCreateUserCommandHandler:
    def test_create_user_command_handler_saves_user(self) -> None:
        user_primitives = UserPrimitivesMother.any()
        command = CreateUserCommand(
            id=user_primitives["id"],
            name=user_primitives["name"],
            age=user_primitives["age"],
        )

        repository = Mock(spec=InMemoryUserRepository)
        handler = CreateUserCommandHandler(repository)

        expected_user = User.from_primitives(command.id, command.name, command.age)

        handler.execute(command)

        repository.save.assert_called_once()
        saved_user = repository.save.call_args[0][0]
        assert saved_user.to_primitives() == expected_user.to_primitives()

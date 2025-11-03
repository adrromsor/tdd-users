from unittest.mock import Mock
from uuid import UUID

from src.application.delete_user.delete_user_command import DeleteUserCommand
from src.application.delete_user.delete_user_command_handler import DeleteUserCommandHandler
from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository
from tests.domain.user_primitives_mother import UserPrimitivesMother


class TestDeleteUserCommandHandler:
    def test_delete_existing_user(self) -> None:
        user_primitives = UserPrimitivesMother.any()
        user = User.from_primitives(
            id=user_primitives["id"],
            name=user_primitives["name"],
            age=user_primitives["age"],
        )

        repository = Mock(spec=InMemoryUserRepository)
        repository.find.return_value = user

        handler = DeleteUserCommandHandler(repository)
        command = DeleteUserCommand(id=user_primitives["id"])

        handler.execute(command)

        repository.find.assert_called_once()
        repository.delete.assert_called_once_with(UUID(user_primitives["id"]))

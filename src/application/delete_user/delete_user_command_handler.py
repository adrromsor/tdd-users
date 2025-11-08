from uuid import UUID

from src.application.delete_user.delete_user_command import DeleteUserCommand
from src.domain.user_not_found_error import UserNotFoundError
from src.domain.user_repository import UserRepository


class DeleteUserCommandHandler:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(self, command: DeleteUserCommand) -> None:
        user = self._repository.find(user_id=UUID(command.id))
        if user is None:
            raise UserNotFoundError(command.id)
        self._repository.delete(user.id)

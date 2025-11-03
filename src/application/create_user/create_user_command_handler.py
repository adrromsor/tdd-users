from src.application.create_user.create_user_command import CreateUserCommand
from src.domain.user import User
from src.domain.user_repository import UserRepository


class CreateUserCommandHandler:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(self, command: CreateUserCommand) -> None:
        user = User.from_primitives(id=command.id, name=command.name, age=command.age)
        self._repository.save(user)

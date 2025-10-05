from src.application.create_user.create_user_command import CreateUserCommand


class CreateUserCommandHandler:
    def execute(self, command: CreateUserCommand) -> None: ...

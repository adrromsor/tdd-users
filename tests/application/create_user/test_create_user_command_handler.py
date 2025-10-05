from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository


class TestCreateUserCommandHandler:
    def test_create_user_command_handler_saves_user(self) -> None:
        command = CreateUserCommand(id="123", name="Mike", age=27)
        repository = Mimic(Spy, InMemoryUserRepository)
        handler = CreateUserCommandHandler(repository)

        handler.execute(command)

        expected_user = User(id="123", name="Mike", age=27)
        expect(repository.save).to(have_been_called_with(expected_user))

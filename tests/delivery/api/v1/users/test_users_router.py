from http.client import CREATED

from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import equal, expect
from fastapi.testclient import TestClient

from main import app
from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.delivery.api.v1.users.users_router import get_create_user_command_handler


class TestUserRouter:
    def test_create_user(self) -> None:
        payload = {"id": "123", "name": "Mike", "age": 27}
        command = CreateUserCommand(id=payload["id"], name=payload["name"], age=payload["age"])
        client = TestClient(app)
        handler = Mimic(Spy, CreateUserCommandHandler)

        app.dependency_overrides[get_create_user_command_handler] = lambda: handler

        response = client.post("/api/v1/users", json=payload)

        expect(response.status_code).to(equal(CREATED))
        expect(handler.execute).to(have_been_called_with(command))

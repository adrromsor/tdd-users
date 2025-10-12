from http.client import CREATED
from unittest.mock import Mock

from fastapi.testclient import TestClient

from main import app
from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.delivery.api.v1.users.users_router import get_create_user_command_handler


class TestUserRouter:
    def test_create_user(self) -> None:
        payload = {"id": "4a079c0b-5474-4648-a836-8cc7c4e4ff3d", "name": "Mike", "age": 27}
        command = CreateUserCommand(id=payload["id"], name=payload["name"], age=payload["age"])
        client = TestClient(app)

        handler = Mock(spec=CreateUserCommandHandler)
        app.dependency_overrides[get_create_user_command_handler] = lambda: handler

        response = client.post("/api/v1/users", json=payload)

        assert response.status_code == CREATED
        handler.execute.assert_called_once_with(command)

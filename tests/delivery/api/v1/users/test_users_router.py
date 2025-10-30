from http.client import CREATED, OK
from unittest.mock import Mock

from fastapi.testclient import TestClient

from main import app
from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.application.search_users.search_users_query_response import SearchUsersQueryResponse
from src.delivery.api.v1.users.users_router import get_create_user_command_handler, get_search_users_query_handler
from tests.domain.user_primitives_mother import UserPrimitivesMother


class TestUserRouter:
    def setup_method(self) -> None:
        self._client = TestClient(app)

    def test_create_user(self) -> None:
        payload = {"id": "4a079c0b-5474-4648-a836-8cc7c4e4ff3d", "name": "Mike", "age": 27}
        command = CreateUserCommand(id=payload["id"], name=payload["name"], age=payload["age"])

        handler = Mock(spec=CreateUserCommandHandler)
        app.dependency_overrides[get_create_user_command_handler] = lambda: handler

        response = self._client.put("/api/v1/users", json=payload)

        assert response.status_code == CREATED
        handler.execute.assert_called_once_with(command)

    def test_search_users(self) -> None:
        users_primitives = [UserPrimitivesMother.any(), UserPrimitivesMother.any()]

        handler = Mock()
        app.dependency_overrides[get_search_users_query_handler] = lambda: handler
        handler.execute.return_value = SearchUsersQueryResponse(users=users_primitives)

        response = self._client.get("/api/v1/users")

        assert response.status_code == OK
        assert response.json() == {"users": users_primitives}

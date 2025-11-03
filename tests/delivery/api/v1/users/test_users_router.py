from http.client import CREATED, OK
from unittest.mock import Mock

from fastapi.testclient import TestClient

from main import app
from src.application.create_user.create_user_command import CreateUserCommand
from src.application.create_user.create_user_command_handler import (
    CreateUserCommandHandler,
)
from src.application.find_user.find_user_query_handler import FindUserQueryHandler
from src.application.find_user.find_user_query_response import FindUserQueryResponse
from src.application.search_users.search_users_query_handler import SearchUsersQueryHandler
from src.application.search_users.search_users_query_response import SearchUsersQueryResponse
from src.delivery.api.v1.users.users_router import (
    get_create_user_command_handler,
    get_find_user_query_handler,
    get_search_users_query_handler,
)
from tests.domain.user_primitives_mother import UserPrimitivesMother


class TestUserRouter:
    def setup_method(self) -> None:
        self._client = TestClient(app)

    def test_create_user(self) -> None:
        user_id = "4a079c0b-5474-4648-a836-8cc7c4e4ff3d"
        payload = {"name": "Mike", "age": 27}
        command = CreateUserCommand(id=user_id, name=payload["name"], age=payload["age"])

        handler = Mock(spec=CreateUserCommandHandler)
        app.dependency_overrides[get_create_user_command_handler] = lambda: handler

        response = self._client.put(f"/api/v1/users/{user_id}", json=payload)

        assert response.status_code == CREATED
        handler.execute.assert_called_once_with(command)

    def test_find_user(self) -> None:
        existing_user_primitives = UserPrimitivesMother.any()
        user_id = existing_user_primitives["id"]

        handler = Mock(spec=FindUserQueryHandler)
        app.dependency_overrides[get_find_user_query_handler] = lambda: handler
        handler.execute.return_value = FindUserQueryResponse(
            id=existing_user_primitives["id"],
            name=existing_user_primitives["name"],
            age=existing_user_primitives["age"],
        )

        response = self._client.get(f"/api/v1/users/{user_id}")

        assert response.status_code == OK
        assert response.json() == existing_user_primitives

    def test_search_users(self) -> None:
        existing_users_primitives = [UserPrimitivesMother.any(), UserPrimitivesMother.any()]

        handler = Mock(spec=SearchUsersQueryHandler)
        app.dependency_overrides[get_search_users_query_handler] = lambda: handler
        handler.execute.return_value = SearchUsersQueryResponse(users=existing_users_primitives)

        response = self._client.get("/api/v1/users")

        assert response.status_code == OK
        assert response.json() == {"users": existing_users_primitives}

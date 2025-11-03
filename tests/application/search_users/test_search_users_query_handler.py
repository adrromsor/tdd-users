from unittest.mock import Mock

from src.application.search_users.search_users_query_handler import SearchUsersQueryHandler
from src.application.search_users.search_users_query_response import SearchUsersQueryResponse
from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository
from tests.domain.user_primitives_mother import UserPrimitivesMother


class TestSearchUsersQueryHandler:
    def test_search_users_query_handler_returns_all_users(self) -> None:
        users_primitives = [UserPrimitivesMother.any(), UserPrimitivesMother.any()]
        users = [
            User.from_primitives(
                id=user_primitives["id"],
                name=user_primitives["name"],
                age=user_primitives["age"],
            )
            for user_primitives in users_primitives
        ]

        repository = Mock(spec=InMemoryUserRepository)
        repository.search.return_value = users

        handler = SearchUsersQueryHandler(repository)

        response = handler.execute()

        assert response == SearchUsersQueryResponse(users=users_primitives)
        repository.search.assert_called_once()

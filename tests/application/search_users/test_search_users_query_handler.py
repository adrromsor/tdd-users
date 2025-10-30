from src.application.search_users.search_users_query_handler import SearchUsersQueryHandler
from src.application.search_users.search_users_query_response import SearchUsersQueryResponse
from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository
from tests.domain.user_primitives_mother import UserPrimitivesMother


class TestSearchUsersQueryHandler:
    def test_search_users_query_handler_returns_all_users(self) -> None:
        repository = InMemoryUserRepository()
        users_primitives = [UserPrimitivesMother.any(), UserPrimitivesMother.any()]

        for user_primitive in users_primitives:
            user = User.from_primitives(
                id=user_primitive["id"],
                name=user_primitive["name"],
                age=user_primitive["age"],
            )
            repository.save(user)

        handler = SearchUsersQueryHandler(repository)

        response: SearchUsersQueryResponse = handler.execute()
        assert response.users == users_primitives

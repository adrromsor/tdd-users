from unittest.mock import Mock

from src.application.find_user.find_user_query import FindUserQuery
from src.application.find_user.find_user_query_handler import FindUserQueryHandler
from src.application.find_user.find_user_query_response import FindUserQueryResponse
from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository
from tests.domain.user_primitives_mother import UserPrimitivesMother


class TestFindUserQueryHandler:
    def test_find_user_query_handler_returns_existing_user(self) -> None:
        user_primitives = UserPrimitivesMother.any()
        user = User.from_primitives(
            id=user_primitives["id"],
            name=user_primitives["name"],
            age=user_primitives["age"],
        )

        repository = Mock(spec=InMemoryUserRepository)
        repository.find.return_value = user

        handler = FindUserQueryHandler(repository)
        query = FindUserQuery(id=user_primitives["id"])

        response: FindUserQueryResponse = handler.execute(query)
        assert response == FindUserQueryResponse(
            id=user_primitives["id"],
            name=user_primitives["name"],
            age=user_primitives["age"],
        )

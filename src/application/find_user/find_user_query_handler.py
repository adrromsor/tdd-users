from uuid import UUID

from src.application.find_user.find_user_query import FindUserQuery
from src.application.find_user.find_user_query_response import FindUserQueryResponse
from src.domain.user_not_found_error import UserNotFoundError
from src.domain.user_repository import UserRepository


class FindUserQueryHandler:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, query: FindUserQuery) -> FindUserQueryResponse:
        user = self._repository.find(user_id=UUID(query.id))
        if user is None:
            raise UserNotFoundError(query.id)
        user_primitives = user.to_primitives()
        return FindUserQueryResponse(id=user_primitives["id"], name=user_primitives["name"], age=user_primitives["age"])

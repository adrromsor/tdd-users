from src.application.search_users.search_users_query_response import SearchUsersQueryResponse
from src.domain.user_repository import UserRepository


class SearchUsersQueryHandler:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(self) -> SearchUsersQueryResponse:
        users = self._repository.search()
        return SearchUsersQueryResponse(users=[user.to_primitives() for user in users])

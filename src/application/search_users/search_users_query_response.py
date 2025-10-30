from dataclasses import dataclass

from src.domain.user import UserPrimitives


@dataclass(frozen=True, kw_only=True)
class SearchUsersQueryResponse:
    users: list[UserPrimitives]

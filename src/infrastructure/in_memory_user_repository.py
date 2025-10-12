from uuid import UUID

from src.domain.user import User
from src.domain.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage: dict[str, User] = {}

    def save(self, user: User) -> None:
        self._storage[user.id] = user

    def find(self, user_id: UUID) -> User | None:
        return self._storage.get(user_id)

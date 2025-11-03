from uuid import UUID

from src.domain.user import User, UserPrimitives
from src.domain.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage: dict[str, UserPrimitives] = {}

    def save(self, user: User) -> None:
        self._storage[str(user.id)] = user.to_primitives()

    def find(self, user_id: UUID) -> User | None:
        user_primitives = self._storage.get(str(user_id))
        if user_primitives is None:
            return None
        return User.from_primitives(user_primitives["id"], user_primitives["name"], user_primitives["age"])

    def search(self) -> list[User]:
        return [
            User.from_primitives(user_primitives["id"], user_primitives["name"], user_primitives["age"])
            for user_primitives in self._storage.values()
        ]

    def delete(self, user_id: UUID) -> None:
        self._storage.pop(str(user_id), None)

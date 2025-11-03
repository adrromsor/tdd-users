from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def find(self, user_id: UUID) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def search(self) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        raise NotImplementedError

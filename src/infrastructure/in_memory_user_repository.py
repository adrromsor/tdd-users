from src.domain.user import User
from src.domain.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def save(self, user: User) -> None: ...

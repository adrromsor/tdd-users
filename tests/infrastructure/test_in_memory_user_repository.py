from expects import equal, expect

from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository


class TestInMemoryUserRepository:
    def test_save_user(self) -> None:
        repository = InMemoryUserRepository()
        user = User(id="123", name="Mike", age=27)

        repository.save(user)

        retrieved = repository.find("123")
        expect(retrieved).to(equal(user))

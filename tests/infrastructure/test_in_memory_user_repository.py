from src.domain.user import User
from src.infrastructure.in_memory_user_repository import InMemoryUserRepository
from tests.domain.user_primitives_mother import UserPrimitivesMother


class TestInMemoryUserRepository:
    def test_save_user(self) -> None:
        repository = InMemoryUserRepository()
        user_primitives = UserPrimitivesMother.any()
        user = User.from_primitives(**user_primitives)  # type: ignore[arg-type]

        repository.save(user)

        retrieved = repository.find(user.id)
        assert retrieved == user

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

    def test_find_existing_user(self) -> None:
        repository = InMemoryUserRepository()
        user_primitives = UserPrimitivesMother.any()
        user = User.from_primitives(**user_primitives)  # type: ignore[arg-type]
        repository.save(user)

        found_user = repository.find(user.id)

        assert found_user is not None
        assert found_user.to_primitives() == user.to_primitives()

    def test_search_returns_all_saved_users(self) -> None:
        repository = InMemoryUserRepository()
        users_primitives = [UserPrimitivesMother.any(), UserPrimitivesMother.any()]
        users = [User.from_primitives(**u) for u in users_primitives]  # type: ignore[arg-type]

        for user in users:
            repository.save(user)

        retrieved = repository.search()

        retrieved_primitives = [u.to_primitives() for u in retrieved]
        assert len(retrieved_primitives) == len(users_primitives)
        assert all(u in retrieved_primitives for u in users_primitives)

    def test_delete_existing_user_removes_it(self) -> None:
        repository = InMemoryUserRepository()
        user_primitives = UserPrimitivesMother.any()
        user = User.from_primitives(**user_primitives)  # type: ignore[arg-type]
        repository.save(user)

        repository.delete(user.id)

        assert repository.find(user.id) is None

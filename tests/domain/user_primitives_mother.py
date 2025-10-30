from uuid import uuid4

from src.domain.user import UserPrimitives


class UserPrimitivesMother:
    ANY_USER_NAME = "Mike"
    ANY_USER_AGE = 27

    @staticmethod
    def any() -> UserPrimitives:
        return UserPrimitives(
            id=str(uuid4()),
            name=UserPrimitivesMother.ANY_USER_NAME,
            age=UserPrimitivesMother.ANY_USER_AGE,
        )

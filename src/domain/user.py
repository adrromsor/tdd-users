from dataclasses import dataclass
from typing import Self, TypedDict
from uuid import UUID


@dataclass
class User:
    id: UUID
    name: str
    age: int

    @classmethod
    def create(cls: type[Self], id: str, name: str, age: int) -> Self:
        return cls.from_primitives(id, name, age)

    @classmethod
    def from_primitives(cls, id: str, name: str, age: int) -> Self:
        return cls(id=UUID(id), name=name, age=age)

    def to_primitives(self) -> "UserPrimitives":
        return UserPrimitives(
            id=str(self.id),
            name=self.name,
            age=self.age,
        )


class UserPrimitives(TypedDict):
    id: str
    name: str
    age: int

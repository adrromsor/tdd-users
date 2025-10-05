from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserCommand:
    id: str
    name: str
    age: int

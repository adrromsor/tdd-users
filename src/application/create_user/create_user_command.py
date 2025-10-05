from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserCommand:
    name: str
    age: int

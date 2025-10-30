from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class CreateUserCommand:
    id: str
    name: str
    age: int

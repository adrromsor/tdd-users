from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class FindUserQueryResponse:
    id: str
    name: str
    age: int

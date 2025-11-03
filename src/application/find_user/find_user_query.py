from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class FindUserQuery:
    id: str

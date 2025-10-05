from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    id: str
    name: str
    age: int

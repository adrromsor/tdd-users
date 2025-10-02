from http.client import CREATED
from fastapi import APIRouter

from src.delivery.api.v1.users.users_requests import UserCreateRequest

users_router = APIRouter()


@users_router.post("/users", status_code=CREATED)
def create_user(user_create_request: UserCreateRequest) -> None: ...

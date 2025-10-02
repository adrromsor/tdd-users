from fastapi import FastAPI

from src.delivery.api.v1.users.users_router import users_router

app = FastAPI()


app.include_router(prefix="/api/v1", router=users_router)

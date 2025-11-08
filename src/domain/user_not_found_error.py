class UserNotFoundError(Exception):
    def __init__(self, user_id: str) -> None:
        super().__init__(f"User with id {user_id} was not found.")

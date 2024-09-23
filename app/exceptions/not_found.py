from fastapi import HTTPException, status


class NotFound(HTTPException):
    def __init__(self, detail: str = "Entity not found.") -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )


class UserNotFound(NotFound):
    def __init__(self) -> None:
        super().__init__(detail="User not found.")

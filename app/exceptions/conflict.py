from fastapi import HTTPException, status


class Conflict(HTTPException):
    def __init__(self, detail: str = "Entity already exists.") -> None:
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail
        )


class UserConflict(Conflict):
    def __init__(self) -> None:
        super().__init__(detail="User already exists.")

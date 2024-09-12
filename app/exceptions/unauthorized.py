from fastapi import HTTPException, status


class Unauthorized(HTTPException):
    def __init__(self, detail: str = "Unauthorized.") -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail
        )


class UserUnauthorized(Unauthorized):
    def __init__(self) -> None:
        super().__init__(detail="User unauthorized.")


class UserWrongCredentials(Unauthorized):
    def __init__(self) -> None:
        super().__init__(detail="Wrong credentials.")

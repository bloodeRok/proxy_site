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


class NotFoundAccessToken(Unauthorized):
    def __init__(self) -> None:
        super().__init__(detail="Access token not found.")


class InvalidToken(Unauthorized):
    def __init__(self) -> None:
        super().__init__(detail="Invalid token.")


class ExpiredToken(Unauthorized):
    def __init__(self) -> None:
        super().__init__(detail="Expired token.")


class NotUserIDToken(Unauthorized):
    def __init__(self) -> None:
        super().__init__(detail="User id not found in token.")

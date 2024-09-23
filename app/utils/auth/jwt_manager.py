from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import Request

from app.exceptions import (
    NotFoundAccessToken,
    InvalidToken,
    ExpiredToken,
    NotUserIDToken
)
from app.utils.constants.config import SECRET, ALGORITHM
from app.utils.constants.defaults import JWT_LIFETIME_SECS, JWT_NAME


class JWTManager:

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(
            seconds=JWT_LIFETIME_SECS
        )
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(
            claims=to_encode,
            key=SECRET,
            algorithm=ALGORITHM
        )
        return encode_jwt

    @staticmethod
    def get_user_id(request: Request) -> int:
        token = request.cookies.get(JWT_NAME)
        if not token:
            raise NotFoundAccessToken()
        try:
            payload = jwt.decode(
                token=token,
                key=SECRET,
                algorithms=[ALGORITHM],
                options={"verify_exp": False}
            )
        except JWTError as e:
            raise InvalidToken()

        expire = payload.get("exp")
        expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
        if (not expire) or (expire_time < datetime.now(timezone.utc)):
            raise ExpiredToken()

        user_id = payload.get("user_id")
        if not user_id:
            raise NotUserIDToken()

        return user_id

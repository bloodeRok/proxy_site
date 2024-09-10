from jose import jwt
from datetime import datetime, timedelta, timezone
from app.utils.constants.config import SECRET, ALGORITHM
from app.utils.constants.defaults import JWT_LIFETIME_SECS


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

from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from app.constants.config import SECRET
from app.constants.defaults import COOKIE_LIFETIME_SECS, JWT_LIFETIME_SECS

cookie_transport = CookieTransport(
    cookie_name="avangard_iau",
    cookie_max_age=COOKIE_LIFETIME_SECS
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=JWT_LIFETIME_SECS)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

from typing import Optional

from fastapi_users import BaseUserManager
from sqlalchemy import select

from app.constants.config import SECRET
from app.exceptions import UserConflict
from app.models import User
from app.repositories.connection import DBConnection


class UserRepository:
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    def __init__(self) -> None:
        self.session = DBConnection().get_session()

    async def create(
        self,
        email: str,
        username: str,
        hashed_password: str
    ) -> User:
        # TODO Validate pass???
        #await self.validate_password(user_create.password, user_create)

        existing_user = await self.get_by_email(email)
        if existing_user is not None:
            raise UserConflict()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user

    async def get_by_email(self, email: str) -> Optional[User]:
        async with self.session as session:
            result = await session.execute(
                select(User).where(User.email == email)
            )
            user = result.scalars().first()
            return user

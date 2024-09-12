from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from app.models import User
from app.repositories.connection import DBConnection


class UserRepository:
    model = User

    def __init__(self) -> None:
        self.session_maker = DBConnection().get_session

    async def create(
            self,
            email: str,
            username: str,
            hashed_password: str,
            is_active: bool,
            is_superuser: bool,
            is_verified: bool,
            session: AsyncSession
    ) -> User:
        created_user = self.model(
            email=email,
            username=username,
            hashed_password=hashed_password,
            is_active=is_active,
            is_superuser=is_superuser,
            is_verified=is_verified,
        )

        session.add(created_user)
        await session.commit()
        await session.refresh(created_user)

        return created_user

    @staticmethod
    async def get_by_email(email: str, session: AsyncSession) -> Optional[User]:
        result = await session.execute(select(User).where(User.email == email))
        return result.scalars().first()

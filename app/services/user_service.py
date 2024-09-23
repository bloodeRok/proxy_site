from fastapi import Response, Depends

from app.exceptions import UserConflict, UserNotFound
from app.exceptions.unauthorized import UserWrongCredentials
from app.models import User
from app.repositories import UserRepository
from app.serializers.schemas import UserCreateSchema, UserLoginSchema
from app.utils.auth.helpers import get_password_hash, verify_password
from app.utils.auth.jwt_manager import JWTManager
from app.utils.constants.defaults import JWT_NAME


class UserService:
    repository = UserRepository()

    async def create(self, new_user: UserCreateSchema) -> User:
        async with self.repository.session_maker() as session:
            existing_user = await self.repository.get_by_email(
                email=new_user.email,
                session=session
            )
            if existing_user is not None:
                raise UserConflict()

            created_user = await self.repository.create(
                email=new_user.email,
                username=new_user.username,
                hashed_password=get_password_hash(password=new_user.password),
                is_active=new_user.is_active,
                is_superuser=new_user.is_superuser,
                is_verified=new_user.is_verified,
                session=session
            )

        return created_user

    async def login(
            self,
            response: Response,
            credentials: UserLoginSchema
    ) -> User:
        async with self.repository.session_maker() as session:
            user = await self.repository.get_by_email(
                email=credentials.email,
                session=session
            )

        if not user:
            raise UserNotFound()

        verify = verify_password(
            plain_password=credentials.password,
            hashed_password=user.hashed_password
        )
        if not verify:
            raise UserWrongCredentials()

        access_token = JWTManager().create_access_token(
            data={"user_id": user.id}
        )
        response.set_cookie(
            key=JWT_NAME,
            value=access_token,
            httponly=True
        )
        return user

    async def get_current_user(
            self,
            user_id=Depends(JWTManager().get_user_id)
    ) -> User:
        async with self.repository.session_maker() as session:
            user = await self.repository.get_by_id(
                user_id=user_id,
                session=session
            )

        if not user:
            raise UserNotFound()
        return user

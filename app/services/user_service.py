from app.exceptions import UserConflict
from app.models import User
from app.repositories import UserRepository
from app.serializers.schemas.user import UserCreateSchema
from app.utils.auth.helpers import get_password_hash


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
                is_verified=new_user.is_verified
            )

            return created_user

from datetime import datetime

from pydantic import BaseModel

from app.serializers.entities_fields import UserFields


class UserCreateSchema(BaseModel):
    email: str = UserFields.email
    password: str = UserFields.password
    username: str = UserFields.username
    is_active: bool = UserFields.is_active
    is_superuser: bool = UserFields.is_superuser
    is_verified: bool = UserFields.is_verified


class UserLoginSchema(BaseModel):
    email: str = UserFields.email
    password: str = UserFields.password


class UserReadSchema(BaseModel):
    id: int = UserFields.id
    email: str = UserFields.email
    username: str = UserFields.username
    registered_at: datetime = UserFields.registered_at
    is_active: bool = UserFields.is_active
    is_superuser: bool = UserFields.is_superuser
    is_verified: bool = UserFields.is_verified

    class Config:
        orm_mode = True

from typing import Optional

from pydantic import BaseModel

from app.serializers.entities_fields import UserFields


class User(BaseModel):
    id: UserFields.id
    email: UserFields.email
    username: UserFields.username
    is_active: UserFields.is_active = True
    is_superuser: UserFields.is_superuser = False
    is_verified: UserFields.is_verified = False

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: UserFields.email
    password: UserFields.password
    username: UserFields.username
    is_active: UserFields.is_active = True
    is_superuser: UserFields.is_superuser = False
    is_verified: UserFields.is_verified = False

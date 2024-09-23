from pydantic import Field


class UserFields:
    id: int = Field(
        title="User ID",
        description="ID пользователя.",
        example=6
    )
    email: str = Field(
        title="User e-mail",
        description="Электронная почта пользователя.",
        example="example@mail.com"
    )
    username: str = Field(
        title="User name",
        description="Имя пользователя.",
        example="John"
    )
    registered_at: str = Field(
        title="User registered at",
        description="Время и дата регистрации пользователя.",
        example="11-06-2024T05:38:47"
    )
    password: str = Field(
        title="User password",
        description="Пароль пользователя.",
        example="123Qwe-"
    )
    is_active: bool = Field(
        title="User is active",
        description="Активен ли пользователь.",
        example=True
    )
    is_superuser: bool = Field(
        title="User is superuser",
        description="Админ ли пользователь.",
        example=False
    )
    is_verified: bool = Field(
        title="User is verified",
        description="Верифицирован ли пользователь.",
        example=False
    )
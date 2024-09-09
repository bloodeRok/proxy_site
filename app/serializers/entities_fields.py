from pydantic import Field


class UserFields:
    id = Field(
        title="User ID",
        description="ID пользователя.",
        example="6"
    )
    email = Field(
        title="User e-mail",
        description="Электронная почта пользователя.",
        example="example@mail.com"
    )
    username = Field(
        title="User name",
        description="Имя пользователя.",
        example="John"
    )
    registered_at = Field(
        title="User regitered at.",
        description="Время и дата регистрации пользователя.",
        example="11-06-2024T05:38:47"
    )
    password = Field(
        title="User password",
        description="Пароль пользователя.",
        example="123Qwe-"
    )
    is_active = Field(
        title="User is active",
        description="Активный ли пользователь.",
        example="True"
    )
    is_superuser = Field(
        title="User is superuser",
        description="Админ ли пользователь.",
        example="False"
    )
    is_verified = Field(
        title="User is verified",
        description="Верифицирован ли пользователь.",
        example="False"
    )

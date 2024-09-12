from fastapi import APIRouter, Response

from app.serializers.request.user import UserReadSerializer
from app.serializers.schemas import UserCreateSchema, UserLoginSchema
from app.services import UserService

router = APIRouter(prefix="/auth", tags=["Auth"])
service = UserService()


@router.post("/register/")
async def user_register(new_user: UserCreateSchema) -> dict:
    user = await service.create(new_user=new_user)

    return {
        "message": "Вы успешно зарегистрированы!",
        "user": UserReadSerializer().serialize(user)
    }


@router.post("/login/")
async def user_login(response: Response, credentials: UserLoginSchema) -> dict:
    user = await service.login(
        credentials=credentials,
        response=response
    )

    return {
        "message": "Вы успешно вошли!",
        "user": UserReadSerializer().serialize(user)
    }

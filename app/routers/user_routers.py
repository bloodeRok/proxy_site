from fastapi import APIRouter, Response, Depends

from app.models import User
from app.serializers.request.user import UserReadSerializer
from app.serializers.schemas import UserCreateSchema, UserLoginSchema
from app.services import UserService
from app.utils.constants.defaults import JWT_NAME

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


@router.get("/me/")
async def get_me(user: User = Depends(service.get_current_user)) -> dict:
    return UserReadSerializer().serialize(user)


@router.post("/logout/")
async def logout_user(response: Response) -> dict:
    response.delete_cookie(key=JWT_NAME)
    return {"message": "Пользователь успешно вышел из системы"}

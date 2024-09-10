from fastapi import APIRouter

from app.serializers.request.user import UserReadSerializer
from app.serializers.schemas.user import UserCreateSchema
from app.services import UserService

router = APIRouter(prefix="/auth", tags=["Auth"])
service = UserService()


@router.post("/register/")
async def register_user(new_user: UserCreateSchema) -> dict:
    user = await service.create(new_user=new_user)

    return {
        "message": "Вы успешно зарегистрированы!",
        "data": UserReadSerializer().serialize(user)
    }

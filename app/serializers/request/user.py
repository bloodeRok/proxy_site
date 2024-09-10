from app.serializers.base_serializer import BaseSerializer
from app.serializers.schemas.user import UserReadSchema

class UserReadSerializer(BaseSerializer):
    model_schema = UserReadSchema
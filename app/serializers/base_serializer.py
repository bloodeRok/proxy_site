import json
from pydantic import BaseModel
from typing import Type

class BaseSerializer:
    model_schema: Type[BaseModel]

    def serialize(self, obj: BaseModel) -> dict:
        fields = self.model_schema.model_fields
        serialized_data = {
            field: getattr(obj, field, None) for field in fields
        }
        return serialized_data

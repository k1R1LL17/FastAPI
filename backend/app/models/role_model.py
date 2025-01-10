from pydantic import BaseModel
from .enums.role_enum import RoleEnum

class Role(BaseModel):
    name:RoleEnum

    def serialize(self):
        data = self.model_dump()
        return data
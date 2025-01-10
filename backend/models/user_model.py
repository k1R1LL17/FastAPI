from pydantic import BaseModel, Field, field_validator
from bson import ObjectId
from dependencies.user_dependencies import validate_age, validate_password
from typing import Optional

class User(BaseModel):
    login: str
    password: str
    name: Optional[str] = None  
    last_name: Optional[str] = None  
    age: Optional[int] = None  
    role_id: Optional[str] = Field(..., description="ID of the role assigned to the user")

    def serialize(self):
        data = self.model_dump()
        return data

    @field_validator("password")
    def strong_password(cls, value):
        return validate_password(value)

    @field_validator("age")
    def check_age(cls, value):
        return validate_age(value)

    @field_validator("role_id")
    def validate_role_id_format(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid role ID format")
        return value

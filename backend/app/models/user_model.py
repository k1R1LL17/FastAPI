from pydantic import BaseModel, Field, field_validator, EmailStr
from bson import ObjectId
from dependencies.user_dependencies import validate_age, validate_password,validate_login,validate_email
from typing import Optional
from utils.password_security import hash_password

class User(BaseModel):
    login: str
    password: str
    name: Optional[str] = None  
    last_name: Optional[str] = None  
    age: Optional[int] = None
    email: EmailStr = None
    role_id: Optional[str] = Field(..., description="ID of the role assigned to the user")

    def serialize(self):
        data = self.model_dump()
        return data

    @field_validator("password")
    def strong_password(cls, value):
        validate_password(value)
        return hash_password(value)

    @field_validator("age")
    def check_age(cls, value):
        return validate_age(value)

    @field_validator("role_id")
    def validate_role_id_format(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid role ID format")
        return value
    
    @field_validator("login")
    def login_exists(cls, value):
        return validate_login(value)

    @field_validator("email")
    def email_exists(cls, value):
        return validate_email(value)
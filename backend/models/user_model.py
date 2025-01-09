from pydantic import BaseModel,field_validator
from dependencies.user_dependencies import validate_age,validate_password

class User(BaseModel):
    login: str
    password: str
    name: str
    last_name: str
    age: int

    def serialize(self):
        data = self.model_dump()
        return data
    
    @field_validator("password")
    def strong_password(cls, value):
        return validate_password(value)

    @field_validator("age")
    def check_age(cls, value):
        return validate_age(value)
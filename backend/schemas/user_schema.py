from pydantic import BaseModel
from models.user_model import User

class UserCreate(User):
    login: str
    password: str
    name: str
    last_name: str
    age: int

class UserResponse(BaseModel):
    id: str
    login: str
    name: str
    last_name: str
    age: int

class UserUpdate(User):
    login: str
    name: str
    last_name: str
    age: int
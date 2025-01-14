from pydantic import BaseModel,EmailStr
from models.user_model import User
from typing import Dict

class UserCreate(BaseModel):
    login: str
    password: str
    name: str
    last_name: str
    age: int
    email:EmailStr
    role_id: str

class UserResponse(BaseModel):
    id: str
    login: str
    name: str
    last_name: str
    age: int
    email:EmailStr
    role_id: str

class UserUpdate(BaseModel):
    login: str
    name: str
    last_name: str
    age: int


class RoleRestriction(BaseModel):
    user_id: str
    role: Dict[str, str]
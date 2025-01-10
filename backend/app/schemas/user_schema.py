from pydantic import BaseModel
from models.user_model import User
from typing import Dict

class UserCreate(User):
    login: str
    password: str
    name: str
    last_name: str
    age: int
    role_id: str

class UserResponse(BaseModel):
    id: str
    login: str
    name: str
    last_name: str
    age: int
    role_id: str

class UserUpdate(User):
    login: str
    name: str
    last_name: str
    age: int

class RoleRestriction(BaseModel):
    user_id: str
    role: Dict[str, str]
from pydantic import BaseModel

class UserCreate(BaseModel):
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

class UserLogin(BaseModel):
    login: str
    password: str
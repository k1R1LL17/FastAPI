from pydantic import BaseModel

class LoginRequest(BaseModel):
    login: str
    password: str

class LoginResponse(BaseModel):
    message: str

class UserRegister(BaseModel):
    login: str
    password: str

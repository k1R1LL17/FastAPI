from pydantic import BaseModel,EmailStr

class LoginRequest(BaseModel):
    login: str
    password: str

class LoginResponse(BaseModel):
    message: str

class UserRegister(BaseModel):
    login: str
    password: str
    email: EmailStr

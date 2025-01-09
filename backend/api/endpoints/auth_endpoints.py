from fastapi import APIRouter, Depends, HTTPException, Response,Request
from schemas.user_schema import UserCreate
from services.auth_service import register_user, login_user,logout_user,get_current_user
from config.config import get_users_collection
from schemas.auth_schema import LoginRequest

router = APIRouter()

@router.post("/register")
def register(
    user: UserCreate,
    response: Response,
    user_collection=Depends(get_users_collection)
):
    return register_user(user_collection, user, response)

@router.post("/login")
def login(
    user: LoginRequest,
    response: Response,
    user_collection=Depends(get_users_collection)
):
    return login_user(user_collection, user.login, user.password, response)

@router.post("/logout")
def logout(response: Response):
    return logout_user(response)

@router.get("/me")
def get_authenticated_user(request: Request):
    user_data = get_current_user(request)
    return {"message": f"Hello, {user_data['sub']}"}
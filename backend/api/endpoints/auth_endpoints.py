from fastapi import APIRouter, Depends, HTTPException, Response,Request
from schemas.user_schema import UserCreate
from services.auth_service import register_user, login_user,logout_user
from config.config import get_users_collection
from schemas.auth_schema import LoginRequest
from utils.jwt_utils import get_current_user

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
def logout(response: Response, current_user = Depends(get_current_user)):
    return logout_user(response)

@router.get("/me")
def get_authenticated_user(request: Request, current_user = Depends(get_current_user)):
    user_data = get_current_user(request)
    return {"message": f"Hello, {current_user}"}
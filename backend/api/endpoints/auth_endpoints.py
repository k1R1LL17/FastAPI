from fastapi import APIRouter, Depends, HTTPException, Response,Request
from schemas.user_schema import UserCreate
from services.auth_service import register_user, login_user,logout_user
from config.config import get_users_collection,get_roles_collection
from schemas.auth_schema import LoginRequest,UserRegister
from utils.jwt_utils import get_current_user

router = APIRouter()

@router.post("/register")
def register(
    user: UserRegister,
    response: Response,
    user_collection=Depends(get_users_collection),
    roles_collection = Depends(get_roles_collection)
):
    return register_user(user_collection, user, response,roles_collection)

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

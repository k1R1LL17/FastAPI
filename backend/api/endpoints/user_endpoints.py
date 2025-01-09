from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import UserCreate, UserResponse
from services.user_service import create_user,get_users,get_user_id
from config.config import get_users_collection 

router = APIRouter()

@router.post("/create/user", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, users_collection = Depends(get_users_collection)):
    return create_user(users_collection, user.model_dump())

@router.get("/get/users",response_model=list[UserResponse])
def get_users_endpoint(users_collection = Depends(get_users_collection)):
    return get_users(users_collection)

@router.get("/get/{user_id}",response_model=UserResponse)
def get_user_id_endpoint(user_id:str, users_collection = Depends(get_users_collection)):
    user = get_user_id(users_collection,user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
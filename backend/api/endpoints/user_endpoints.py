from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import UserCreate, UserResponse,UserUpdate
from services.user_service import create_user,get_users,get_user_id,update_user,delete_user
from config.config import get_users_collection 
from pymongo.collection import Collection

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

@router.put("/update/{user_id}",response_model = UserResponse)
def update_user_endpoint(user_id:str, user:UserUpdate, users_collection = Depends(get_users_collection)):
    updated_user = update_user(users_collection, user_id, user.model_dump())
    
    if updated_user:
        return updated_user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/delete/user/{user_id}")
def delete_user_endpoint(user_id: str, user_collection = Depends(get_users_collection)):
    deleted = delete_user(user_collection, user_id)
    if deleted:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
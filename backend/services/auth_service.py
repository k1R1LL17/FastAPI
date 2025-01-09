from fastapi import HTTPException, Response, Request
from utils.jwt_utils import create_access_token, decode_access_token
from utils.password_security import verify_password
from pymongo.collection import Collection
from schemas.user_schema import UserCreate
from services.user_service import create_user

def login_user(db:Collection, login: str, password: str, response: Response):
    db_user = db.find_one({"login":login})

    if not db_user or not verify_password(password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid login credentials")
    
    access_token = create_access_token(data={"sub": db_user["_id"]})

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,  
        samesite="Lax",
    )
    return {"message": "Login successful"}

def logout_user(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out successfully"}

def register_user(user_collection:Collection, user_data: UserCreate, response: Response):
    created_user = create_user(user_collection, user_data.model_dump())
    access_token = create_access_token(data={"sub": created_user["_id"]})
    
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,  
        samesite="Lax",
    )
    return {"message": "User has registered successfully"}
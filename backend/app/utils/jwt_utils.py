import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Request, Depends
from fastapi.security import OAuth2PasswordBearer
from bson import ObjectId
from config.config import get_users_collection,get_roles_collection
from schemas.user_schema import RoleRestriction

SECRET_KEY = "some_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()

    if isinstance(to_encode.get("sub"), ObjectId):
        to_encode["sub"] = str(to_encode["sub"])

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(
    request: Request,
    user_collection=Depends(get_users_collection),
    roles_collection=Depends(get_roles_collection),
):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    decoded_token = decode_access_token(token)
    user_id = decoded_token.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Token does not contain user ID")
    
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    user_role_id = user.get("role_id")
    user_role = roles_collection.find_one({"_id": ObjectId(user_role_id)})

    if not user_role:
        raise HTTPException(status_code=401, detail=f"Role not found: {user_role_id}")

    role_response = {
        "_id": str(user_role["_id"]),
        "name": user_role["name"]
    }

    return RoleRestriction(user_id=str(user_id), role=role_response)

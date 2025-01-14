from fastapi import HTTPException
import re
from config.config import get_users_collection
from pymongo.collection import Collection

def validate_age(age: int):
    if age <= 12:
        raise HTTPException(status_code=400, detail="Age must be greater than 12.")
    return age

def validate_password(password: str):
    if len(password) < 8 or not re.search(r'[A-Z]', password) or not re.search(r'\d', password) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters long, contain one uppercase letter, one number, and one special character."
        )
    return password

def validate_login(login: str):
    users_collection: Collection = get_users_collection()

    if users_collection.find_one({"login": login}):
        raise HTTPException(
            status_code=400,
            detail="This login already exists"
        )
    
    return login

def validate_email(email:str):
    users_collection: Collection = get_users_collection()

    if users_collection.find_one({"email": email}):
        raise HTTPException(
            status_code=400,
            detail="This email already exists"
        )
    
    return email
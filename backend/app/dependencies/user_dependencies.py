from fastapi import HTTPException
import re

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
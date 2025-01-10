from fastapi import Depends, HTTPException
from models.enums.role_enum import RoleEnum
from .jwt_utils import get_current_user

def role_required(role: RoleEnum):
    def wrapper(current_user = Depends(get_current_user)):
        user_role = current_user.role.get('name')
        
        if user_role != role.value:
            raise HTTPException(status_code=403, detail="You don't have permission")
        
        return current_user
    return wrapper

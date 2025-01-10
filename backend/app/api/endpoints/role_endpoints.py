from schemas.role_schema import Role,RoleResponse
from fastapi import APIRouter, Depends,HTTPException
from config.config import get_roles_collection
from utils.jwt_utils import get_current_user
from services.role_service import create_role,get_roles,update_role,delete_role
router = APIRouter()

@router.post("/create/role", response_model=Role)
def create_user_endpoint(role: Role, roles_collection = Depends(get_roles_collection), current_user = Depends(get_current_user)):
    return create_role(roles_collection, role.model_dump())

@router.get("/get/roles",response_model=list[RoleResponse])
def get_users_endpoint(roles_collection = Depends(get_roles_collection), current_user = Depends(get_current_user)):
    return get_roles(roles_collection)

@router.put("/update/{role_id}",response_model = Role)
def update_user_endpoint(role_id:str, role:Role, roles_collection = Depends(get_roles_collection), current_user = Depends(get_current_user)):
    updated_user = update_role(roles_collection, role_id, role.model_dump())
    
    if updated_user:
        return updated_user
    else:
        raise HTTPException(status_code=404, detail="Role not found")
    
@router.delete("/delete/user/{role_id}")
def delete_user_endpoint(role_id: str, roles_collection = Depends(get_roles_collection), current_user = Depends(get_current_user)):
    deleted = delete_role(roles_collection, role_id)
    if deleted:
        return {"message": "Role deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Role not found")
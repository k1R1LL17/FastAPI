from pydantic import BaseModel
from models.role_model import Role

class Role(Role):
    name:str

class RoleResponse(BaseModel):
    id:str
    name:str
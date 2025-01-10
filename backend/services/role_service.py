from models.role_model import Role
from pymongo.collection import Collection
from bson import ObjectId

def create_role(db:Collection,role_data:dict):
    role = Role(**role_data)
    result = db.insert_one(role.serialize())
    return {**role.serialize(), "id": str(result.inserted_id)}

def get_roles(db:Collection)->list[dict]:
    return[
        {**doc,"id":str(doc["_id"])} for doc in db.find()
    ]

def update_role(db: Collection, role_id: str, role_data: dict) -> dict:
    update_fields = {key: value for key, value in role_data.items() if value is not None}

    result = db.update_one(
        {"_id": ObjectId(role_id)},  
        {"$set": update_fields}  
    )

    if result.matched_count > 0:
        updated_user = db.find_one({"_id": ObjectId(role_id)})
        return {**updated_user, "id": str(updated_user["_id"])}
    else:
        return None
    
def delete_role(db:Collection, role_id:str) -> bool:
    result = db.delete_one({"_id": ObjectId(role_id)})
    return result.deleted_count > 0
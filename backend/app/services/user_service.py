from pymongo.collection import Collection
from bson import ObjectId
from models.user_model import User
from utils.password_security import hash_password

def create_user(db:Collection, user_data:dict):
    user_data["password"] = hash_password(user_data["password"])
    user = User(**user_data)
    result = db.insert_one(user.serialize())
    return {**user.serialize(), "id": str(result.inserted_id)}

def get_users(db:Collection)->list[dict]:
    return[
        {**doc,"id":str(doc["_id"])} for doc in db.find()
    ]

def get_user_id(db:Collection, user_id:str) -> dict:
    user = db.find_one({"_id":ObjectId(user_id)})
    if user:
        return {**user, "id": str(user["_id"])}
    return None

def update_user(db: Collection, user_id: str, user_data: dict) -> dict:

    update_fields = {key: value for key, value in user_data.items() if value is not None}

    result = db.update_one(
        {"_id": ObjectId(user_id)},  
        {"$set": update_fields}  
    )

    if result.matched_count > 0:
        updated_user = db.find_one({"_id": ObjectId(user_id)})
        return {**updated_user, "id": str(updated_user["_id"])}
    else:
        return None

def delete_user(db:Collection, user_id:str) -> bool:
    result = db.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0
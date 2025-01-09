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

from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("mongodb+srv://admin:admin@cluster0.pxcvj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.game_shop

def get_users_collection() -> Collection:
    """Dependency function to return the MongoDB users collection."""
    return db["users"]
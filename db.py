from pymongo import MongoClient
from user import User

client = MongoClient("mongodb+srv://test:test@chatapp.dn4u7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users")


def save_user(username, email, password):
    # username is primary key, password isn't hashed cuz it's just an example
    users_collection.insert_one({'_id': username, 'email': email, 'password': password})

def get_user(username):
    user_data = users_collection.find_one({"_id": username})
    return User(user_data["_id"], user_data["email"], user_data["password"]) if user_data else None

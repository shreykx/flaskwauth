from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient('mongodb://localhost:27017/')
db = client.redspace

def CheckUser(username, password):
    collection = db.users
    if collection.find_one({'username': username, 'password': password}):
        return True
    else:
        return False

def CreateUser(username, password):
    collection = db.users
    try:
        result = collection.insert_one({
            'username': username,
            'password': password
        })
        return True
    except DuplicateKeyError:
        return False

# Ensure that the 'username' field is unique by creating an index
collection = db.users
collection.create_index('username', unique=True)

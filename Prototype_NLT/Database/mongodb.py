from pymongo import MongoClient
from Database import config

def connection_mongodb():
    client = MongoClient(config.DATABASE_URL)
    db = client[config.DATABASE_NAME]
    collection = db.utilisateurs
    return client, collection

def insert_in_database(prompt, result, name):
    client, collection = connection_mongodb()
    collection.insert_many([{"prompt": prompt, "result": result, "username": name}])
    client.close()

def get_database(name):
    client, collection = connection_mongodb()
    return collection.find({"username": name}), client

def close_connection(client):
    client.close()

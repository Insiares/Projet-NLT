from pymongo import MongoClient
from Database import config

def connect_mongodb():
    """
    Establishes a connection to MongoDB.

    Returns:
        client: The MongoDB client.
        collection: The 'utilisateurs' collection.
    """
    # Establish a connection to the MongoDB server
    client = MongoClient(config.DATABASE_URL)
    
    # Access the desired database
    db = client[config.DATABASE_NAME]
    
    # Access the 'utilisateurs' collection in the database
    collection = db.utilisateurs
    
    # Return the client and the 'utilisateurs' collection
    return client, collection
def insert_in_database(prompt, result, name):
    """
    This function inserts a document into a MongoDB collection.
    
    Args:
        prompt (str): The prompt for the document.
        result (str): The result for the document.
        name (str): The username for the document.
    """
    # Establish MongoDB connection and get the collection
    client, collection = connect_mongodb()
    
    # Insert the document into the collection
    collection.insert_many([
        {"prompt": prompt, "result": result, "username": name}
    ])
    
    # Close the MongoDB connection
    client.close()

def get_database(name):
    """
    This function connects to a MongoDB database and retrieves the collection
    with the given name.

    Parameters:
    name (str): The name of the collection to retrieve.

    Returns:
    tuple: A tuple containing the collection and the MongoDB client.
    """
    # Establish a connection to MongoDB
    client, collection = connect_mongodb()

    # Find documents in the collection with the given username
    result = collection.find({"username": name})

    # Return the result and the MongoDB client
    return result, client

def close_connection(client):
    """
    This function closes the connection with the client.

    Args:
        client: The client object to close the connection with.
    """
    # Close the connection with the client
    client.close()

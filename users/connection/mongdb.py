import pymongo
from connection.secrets import settings

password= settings.database_password
user = settings.database_username
database = settings.database_name
collection = settings.database_collection

client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@cluster0.bqmxnfo.mongodb.net/?retryWrites=true&w=majority")
db = client[database]
users_collection = db[collection]



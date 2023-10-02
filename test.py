from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ziyanshabbir25:Pakistan204@cluster0.fow6lsm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Connected")
    mydb = client["mydatabase"]
    mycol = mydb["customers"]

    print(mydb.list_collection_names())
    mydict = { "name": "Joh111n", "address": "Highway 37" }

    x = mycol.insert_one(mydict)
    print(x)
except Exception as e:
    print(e)
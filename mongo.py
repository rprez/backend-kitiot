from pymongo import MongoClient
import os

mongo_uri = os.environ.get('MONGO_URI')

if not(mongo_uri):
    print(f"Not connection to MongoDB: {mongo_uri}")
else:
    client = MongoClient(mongo_uri)
    db = client.kit
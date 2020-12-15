from pymongo import MongoClient
import os
from urllib import parse

#Mongo URI
#Example: mongodb://mongoadmin:secret@172.17.0.3:27017

mongo_username = os.environ.get('MONGO_USER')
mongo_password = os.environ.get('MONGO_PASSWORD')
mongo_ip = os.environ.get('MONGO_IP')
mongo_port = os.environ.get('MONGO_PORT')

if not(mongo_username) and (mongo_password) and {mongo_ip} and {mongo_port}:
    print(f"Not env varible set: {mongo_username} {mongo_password} {mongo_ip} {mongo_port}")
else:

    mongo_uri = f"mongodb://{parse.quote(mongo_username)}:{parse.quote(mongo_password)}@{mongo_ip}:{mongo_port}/"
    client = MongoClient(mongo_uri)
    db = client.kit
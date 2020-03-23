import pymongo
import os
import json

f = open("config/db_k", "r")
st=f.read().split()
location = os.getcwd()
with open(location+'/artist_details.json') as f:
  data = json.load(f)
uri="mongodb://"+st[0]+":"+st[1]+"@cluster0-shard-00-00-9q5sm.mongodb.net:27017,cluster0-shard-00-01-9q5sm.mongodb.net:27017,cluster0-shard-00-02-9q5sm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)

#To check the connection to DB
# try:
#     print("MongoDB version is %s" %client.server_info()['version'])
# except pymongo.errors.OperationFailure as error:
#     print(error)
#     quit(1)

# print(client.list_database_names())
# print(db.list_collection_names())

#upload artist to DB
db=client["choraleDB"]
col=db["artist"]
x=col.insert_many(data)
print(x.inserted_ids)





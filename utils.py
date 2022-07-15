from pymongo import mongo_client
import pymongo

connection_string = 'mongodb://root:password@mongo:27017/'
client = pymongo.MongoClient(connection_string)
storedb = client['storefront']

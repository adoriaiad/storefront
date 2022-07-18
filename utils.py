from pymongo import mongo_client
import pymongo
from django.conf import settings

client = pymongo.MongoClient(settings.DB_NAME)
# define the database name
db = client['mongo']
# get/create collection name
customer_coll = db["customer"]

customer1 = {
    "name": "Pinco",
    "surname": "Pallo"
}
customer2 = {
    "name": "Tizio",
    "surname": "Caio"
}
customer3 = {
    "name": "Brunilla",
    "surname": "Bruni"
}

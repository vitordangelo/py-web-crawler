import pymongo
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://vitor:ednA89NDcAeOJyYa@cluster0-xvldm.gcp.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")

db = client.scraping

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}

result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

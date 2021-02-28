import pymongo
import os

password = os.environ.get("PASSWORD", "")
cluster = os.environ.get("CLUSTER", "")

# client = pymongo.MongoClient('localhost', 27017)
client = pymongo.MongoClient("mongodb+srv://sayftest:" + password + "@" + cluster + ".mongodb.net/test?retryWrites=true&w=majority")
db = client.test

posts = db.demo

post_data = {
    'title': 'Python and MongoDB',
    'content': 'Test using PyMongo',
    'author': 'Sayf'
}
post_id = posts.insert_one(post_data).inserted_id

# pause
input("Check MongoDB")

data = posts.find_one({'_id': post_id})
print(data)




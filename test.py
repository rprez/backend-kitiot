from pymongo import MongoClient

client = MongoClient("172.17.0.2",27017,username='admin',password='kitiot')

db = client['pymongo_test']
posts = db.posts

post_data = {
    'title': 'Python and MongoDB',
    'author': 'Scott'
}
new_value = {
    "$set": { "content": "Update Content" }
}
result = posts.update(post_data,new_value)

bills_post = posts.find({'author': 'Scott'})
for post in bills_post:
    print(post)
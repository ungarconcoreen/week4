from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta

# db.users.insert_one({'name':'Stpehen','age': 32})
# db.users.insert_one({'name':'Klay','age':35})

# db.users.insert_one({'name':'Durant','age':45},{'name':'Andre','age':55})




# all_users = db.users.find()
#
# print(all_users[])

# print(all_users[0]['name'])
#
# for user in all_users:
#     print(user)
#
# user = db.users.find_one({'name':'bobby'},{'_id':0})

db.users.update_one({'name':'bobby'},{'$set':{'age':19}
# user = db.users.find_one({'name':'bobby'})
user = db.users.find_one({'name':'bobby'})

print(user)
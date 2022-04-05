from pymongo import MongoClient

con = MongoClient()

# print(con.local.user.insert_one({"ne": "rioine"}))
print(list(con.local.user.find()))
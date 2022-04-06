from pymongo import MongoClient

con = MongoClient()

db = con.local

# print(db.user.insert_one({"ne": "rioine"}))
print(list(db.user.find()))
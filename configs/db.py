from pymongo import MongoClient

con = MongoClient()

print(con.local.user.insert_one({"name": "rioine"}))
print(list(con.local.user.find()))
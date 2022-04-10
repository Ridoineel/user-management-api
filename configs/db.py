from pymongo import MongoClient

# put your mongodb uri here
# con = MongoClient(DB_URI)

# if u wanna to use local
con = MongoClient()

# by default
db = con.local
from pymongo import MongoClient
from dotenv import dotenv_values

 # get database uri from .env file
DB_URI = dotenv_values().get("DB_URI")

if DB_URI:
	con = MongoClient(DB_URI)
else:
	con = MongoClient()

# by default bb name is local
db = con.local

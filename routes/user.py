from fastapi import APIRouter
from fastapi import HTTPException
from typing import List
from re import match
from uuid import uuid4
from uuid import UUID
from bson.objectid import ObjectId
from models.user import *
from utils.functions import encrypt
from configs.db import con
from schemas.user import userEntity
from schemas.user import parseMgEntity


user = APIRouter()

# db: List[User] = [
# 	User(
# 		first_name="Jamila",
# 		last_name="Ahmed",
# 		username="ah12",
# 		password="kjdfkje",
# 		gender=Gender.female,
# 		roles=[Role.user]
# 	),
# 	User(
# 		first_name="Ridoine",
# 		last_name="OURO",
# 		username="ouro454",
# 		password="5587455",
# 		gender=Gender.male,
# 		roles=[Role.admin, Role.user]
# 	),
# 	User(
# 		first_name="Grâce",
# 		last_name="BOHN",
# 		username="boh545",
# 		password="8879455",
# 		gender=Gender.female,
# 		roles=[Role.user]
# 	),
# ]

def usernameExist(username: str):
	""" Check if the user exist

	"""

	user = con.local.user.find_one({"username": username})
	
	if user:
		return True

	return False


@user.get("/users")
async def fetch_users():
	return list(map(parseMgEntity, con.local.user.find()))

@user.get("/users/{_id}")
async def get_user(_id):
	user = con.local.user.find_one({"_id": ObjectId(_id)})

	if user:
		user["id"] = str(user["_id"])
		del user["_id"]

		return user

	# user not exist
	raise HTTPException(
			status_code=404,
			detail={
				"error_message": "user not found"
			}
			
		)

@user.post("/users/signup")
async def signup(user: UserSignupModel):
	""" register user

	"""

	username = user.username.strip().lower()
	first_name = user.first_name.strip().lower()
	last_name = user.last_name.strip().upper()
	gender = user.gender.strip().lower()
	password = user.password
	password2 = user.password2
	roles = user.roles

	### check if data is valid ###
	error_messages = []

	# check if username
	if match(r"^[a-z][a-z0-9]{2,}$", username) is None:
		# invalid username
		error_messages.append("invalid username")

	if match(r"^[A-Z\-']+$", last_name) is None:
		# last name is invalid
		error_messages.append("invalid last_name")

	if match(r"^[a-z]{2,}$", first_name) is None:
		# first name is invalid
		error_messages.append("invalid first_name")

	if gender not in [Gender.female, Gender.male]:
		# gender is invalid
		error_messages.append("invalid gender")

	if len(set(roles) & {Role.user, Role.admin}) != len(roles):
		# roles is invalid
		error_messages.append("invalid roles")

	if password != password2:
		# password and password2 not match
		error_messages.append("the two passwords (password & password2) are differents")

	if len(password) < 6:
		# invalid password
		error_messages.append("password length must be greather than 5")

	if error_messages:
		raise HTTPException(
			status_code=404,
			detail={
				"error_messages":error_messages
			}
			
		)


	############################

	# All data is valid

	user = User(
		first_name = first_name,
		last_name = last_name,
		username = username,
		password = encrypt(password),
		gender = gender,
		roles = roles
	)

	if usernameExist(username):
		raise HTTPException(
			status_code=404,
			detail={
				"error_message": "username is already be taken"
			}
			
		)

	# All is done

	# add user to db
	con.local.user.insert_one(userEntity(user))

	_id = con.local.user.find_one({"username": username})["_id"]


	return {"id": str(_id)}

@user.post("/users/signin")
async def signin(user: UserSigninModel):
	""" user authentification 

	"""

	username = user.username.strip().lower()
	password = encrypt(user.password)

	user = con.local.user.find_one({
			"username": username, 
			"password": password
		})

	if user:
		return {"id": str(user["_id"])}

	# if user not exist
	raise HTTPException(
				status_code=404,
				detail={
					"error_message": "User not exist"
				}
			)


@user.put("/users/{user_id}")
async def update_user(data: UserUpdateRequest, user_id):
	

	print(type(data))
	print(list(user_id))
	exit()

	user = con.local.user.find_one({"_id": ObjectId(user_id)})

	if user:
		con.local.user.update_one({"_id": ObjectId(dict(user_id))}, 
								{"$set": data})
	
		return {
			"status": 200
		}

	raise HTTPException(
			status_code=404,
			detail=f"user with id: {user_id} does not exist"
		)

@user.delete("/users/{user_id}")
async def delete_user(user_id):

	res = con.local.user.delete_one({"_id": ObjectId(user_id)})

	if res.deleted_count == 1:
		# success deletion

		return {
				"status": 200
			}

	raise HTTPException(
			status_code=404,
			detail=f"user with id: {user_id} does not exist"
		)
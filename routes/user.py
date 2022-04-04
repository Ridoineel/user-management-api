from fastapi import APIRouter
from fastapi import HTTPException
from typing import List
from uuid import uuid4
from uuid import UUID
from models.user import *
from re import match
from utils.functions import encrypt

user = APIRouter()

db: List[User] = [
	User(
		first_name="Jamila",
		last_name="Ahmed",
		username="ah12",
		password="kjdfkje",
		gender=Gender.female,
		roles=[Role.user]
	),
	User(
		first_name="Ridoine",
		last_name="OURO",
		username="ouro454",
		password="5587455",
		gender=Gender.male,
		roles=[Role.admin, Role.user]
	),
	User(
		first_name="Grâce",
		last_name="BOHN",
		username="boh545",
		password="8879455",
		gender=Gender.female,
		roles=[Role.user]
	),
]

def usernameExist(username: str):
	""" Check if the user exist

	"""

	for user in db:
		if user.username == username:
			return True

	return False

def userExist(user: User):
	if not usernameExist(user.username):
		return False

	for u in db:
		if u.username == user.username and u.password == user.password:
			return True

	return False


@user.get("/users")
async def fetch_users():
	return db

@user.get("/users/{_id}")
async def get_user(_id: UUID):
	for user in db:
		if user.id == _id:
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
	db.append(user)

	return {"id": db[-1].id}

@user.post("/users/signin")
async def signin(user: UserSigninModel):
	""" user authentification 

	"""

	username = user.username.strip().lower()
	password = encrypt(user.password)

	for u in db:
		if (u.username == username) and (u.password == password):
			# user exist

			return {
				"id": u.id,
			}

	# if user not exist
	raise HTTPException(
				status_code=404,
				detail={
					"error_message": "User not exist"
				}
			)


@user.put("/users/{user_id}")
async def update_user(data: UserUpdateRequest, user_id: UUID):
	for user in db:
		if user.id == user_id:
			for field, value in data:
				if field is not None:
					# field is string
					# so it's impossible to do
					# user.field = value
					# but with exec function, 
					# it's possible
					exec(f"user.{field} = value")

			return {
				"status": 200
			}

	raise HTTPException(
			status_code=404,
			detail=f"user with id: {user_id} does not exist"
		)

@user.delete("/users/{user_id}")
async def delete_user(user_id: UUID):

	for user in db:
		if user.id == user_id:
			# delete user
			db.remove(user)

			return {
				"status": 200
			}

	raise HTTPException(
			status_code=404,
			detail=f"user with id: {_id} does not exist"
		)
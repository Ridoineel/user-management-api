from pydantic import BaseModel
from typing import Optional
from typing import List
from uuid import UUID 
from uuid import uuid4
from enum import Enum


class Gender(str, Enum):
	male = "male"
	female = "female"

class Role(str, Enum):
	admin = "admin"
	user = "user"
 
class User(BaseModel):
	id: Optional[UUID]
	first_name: str
	last_name: str
	username: str
	password: str
	gender: Gender
	roles: Optional[List[Role]] = [Role.user]

	def __init__(self, **params):
		params["id"] = uuid4()

		super().__init__(**params)

	def __getitem__(self, item):
		obj = {
			"id": self.id,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"gender": self.gender,
			"roles": self.roles
		}

		if item in obj:
			return obj[item]
		else:
			raise KeyError(f"{item}")

	def __setitem__(self, item, value):
		items = ["id", 
			"first_name", 
			"last_name", 
			"gender", 
			"roles"
			]

		if item in items:
			exec(f"self.{item} = value")
		else:
			raise KeyError(f"{item}")

class UserSignupModel(User, BaseModel):
	password2: str


class UserSigninModel(BaseModel):
	username: str
	password: str

class UserUpdateRequest(BaseModel):
	first_name: Optional[str]
	last_name: Optional[str]
	roles: Optional[List[Role]]


	def __getitem__(self, item):
		obj = {
			"first_name": self.first_name,
			"last_name": self.last_name,
			"roles": self.roles
		}

		if item in obj:
			return obj[item]
		else:
			raise KeyError(f"{item}")
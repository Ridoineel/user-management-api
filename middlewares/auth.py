from fastapi import Header
from typing import Optional
import jwt
from dotenv import dotenv_values

 # get token secret
TOKEN_SECRET = dotenv_values().get("TOKEN_SECRET")

def auth(authorization: Optional[str] = Header(None)):

	# autorization = "xxxxx <token>"
	token = authorization.split()[1]

	decoded_user_id = jwt.decode(token, TOKEN_SECRET, algorithm="HS256")["user_id"]

	if decoded_user_id == user_id:
		# user is authentificated
		return True
	
	# is not...
	return False

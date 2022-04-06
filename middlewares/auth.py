from fastapi import Request
# import jwt

def auth(req: Request):

	# token = req.header.token
	# user_id = jwt.decode(token, "secret", algorithm="HS256")["user_id"]

	# if user_id == req.body.id:
	# 	# user is authentificated
	# 	return True
	
	# is not...
	return False


def userEntity(user):
	return {
			"first_name": user.first_name,
			"last_name": user.last_name,
			"username": user.username,
			"password": user.password,
			"gender": user.gender,
			"roles": user.roles
		}

def parseMgEntity(user):
	return {
			"id": str(user["_id"]),
			"first_name": user["first_name"],
			"last_name": user["last_name"],
			"username": user["username"],
			"password": user["password"],
			"gender": user["gender"],
			"roles": user["roles"]
		}
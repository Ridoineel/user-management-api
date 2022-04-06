from fastapi import FastAPI
from fastapi import Request
from fastapi import HTTPException
from routes.user import *
from middlewares.auth import auth

app = FastAPI()

app.include_router(user)

# @app.middleware("http")
# async def auth_checker(req: Request, call_next):
# 	print(dir(call_next))
# 	print(call_next.__code__)
# 	if call_next == call_next:
# 		# verify authentification
# 		if auth(req):
# 			return await call_next(req)
		
# 		return {"f": "ddd"}
# 		# print(11111111111)
# 		# # if user is not authenificated
# 		# raise HTTPException(
# 		# 	status_code=404,
# 		# 	detail={
# 		# 		"error_message": "access unautorised"
# 		# 	}
# 		# )
# 	else:
# 		res = await call_next(req)

# 		return res



@app.get("/")
async def root():
	return {
		"API": "User management api",
		"name": "RidoneEl (Ridoine OURO-BANG'NA)"
	}
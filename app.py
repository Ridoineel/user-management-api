from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.include_router(user)

# app.add_route("/user", user)

@app.get("/")
async def root():
	return {
		"API": "User management api",
		"name": "RidoneEl (Ridoine OURO-BANG'NA)"
	}
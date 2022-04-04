from requests import post
from requests import get
from requests import delete
from requests import put
from json.decoder import JSONDecoder
from json.encoder import JSONEncoder

json_decode = JSONDecoder().decode
json_encode = JSONEncoder().encode

def main():
	signup_data = {
		"first_name": "Ridoine",
		"last_name": "OURO-BANG'NA",
		"username": "ridoineel",
		"gender": "male",
		"password": "ridi96",
		"password2": "ridi96"
	}

	signin_data = {
		"username": "RidoineEl", 
		"password": "ridi96"
	}

	signup_result = post("http://localhost:8000/users/signup", 
					json_encode(signup_data))
	signin_result = post("http://localhost:8000/users/signin", 
					json_encode(signin_data))

	
	print("Signup")
	print(signup_result)
	signup_result = json_decode(signup_result.text)
	print(signup_result)

	get_result = get("http://localhost:8000/users/%s" % json_decode(signin_result.text)["id"])

	print()

	print("Signin")
	print(signin_result)
	print(signin_result.text)

	print()
	print("Get user")
	print(get_result.text)

if __name__ == '__main__':
	main()
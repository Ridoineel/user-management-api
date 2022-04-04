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
		"username": "Ridoine", 
		"password": "marks"
	}

	# signin_result = post("http://localhost:8000/api/v1/users/signin", 
	# 				json_encode(signin_data))
	signup_result = post("http://localhost:8000/api/v1/users/signup", 
					json_encode(signup_data))

	print("Signup")
	print(signup_result)
	print(signup_result.text)

	print()

	# print("Signin")
	# print(signin_result)
	# print(signin_result.text)

if __name__ == '__main__':
	main()
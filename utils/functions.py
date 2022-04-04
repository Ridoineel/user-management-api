from hashlib import sha256

def crypt(string):
	encoded_string = string.encode()

	return sha256(encoded_string).hexdigest()
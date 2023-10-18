# The functions required for an affine cipher, with the given key parameters and an alphabet function

import alphabet

# Returns the inverse of a number in modulo m (within Z_m) or None if the number has no inverse
def inverse(a : int, mod : int) -> int:
	for x in range(1, 27):
		if (x*a % mod) == 1:
			return x
	return None

# Encrypts the given text using an affine cipher with the given keys a,b utilising the given alphabet function
# The expected specification of the alphabet function: 
#  when the given parameter is a letter, the corresponding number is returned, when given parameter is a number, the corresponding letter is returned, when None is given, the modulus is returned
def encrypt(text : str, a : int, b : int, alphabet) -> str:
	result = ""
	for c in text:
		if c == ' ':
			result += ' '
		else:
			idx = alphabet(c)
			newIdx = (int(a) * idx + int(b)) % 26
			result += alphabet(newIdx)
	return result

# Decrypts the given text using an affine cipher with the given keys a,b utilising the given alphabet function
# The expected specification of the alphabet function: 
#  when the given parameter is a letter, the corresponding number is returned, when given parameter is a number, the corresponding letter is returned, when None is given, the modulus is returned
def decrypt(text : str, a : int, b : int, alphabet) -> str:
	result = ""
	inv = inverse(int(a), alphabet(None))
	if inv is None:
		print("Deciphering error - given key 'a' invalid")
		return None

	for c in text:
		if c == ' ':
			result += ' '
		else:
			idx = alphabet(c)
			newIdx = ((idx - int(b)) * inv) % 26
			result += alphabet(newIdx)
	return result


# Encrypts the given text using an affine cipher in a standard Z_26 alphabet
def encrypt26(text : str, a : int, b : int) -> str:
	return encrypt(text, a, b, alphabet.standard)

# Decrypts the given text using an affine cipher in a standard Z_26 alphabet
def decrypt26(text : str, a : int, b : int) -> str:
	return decrypt(text, a, b, alphabet.standard)

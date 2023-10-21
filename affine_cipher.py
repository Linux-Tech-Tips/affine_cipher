# The functions required for an affine cipher, with the given key parameters and an alphabet function

import alphabet

# Returns the inverse of a number in modulo m (within Z_m) or None if the number has no inverse
def inverse(a : int, mod : int) -> int:
	for x in range(1, mod):
		if (x*a % mod) == 1:
			return x
	return None

# Encrypts the given text using an affine cipher with the given keys a,b utilising the given alphabet function
# The expected specification of the alphabet function: 
#  when the given parameter is a letter, the corresponding number is returned, when given parameter is a number, the corresponding letter is returned, when None is given, the modulus is returned
def encrypt(text : str, a : int, b : int, alphabet) -> str:
	result = ""
	extChars = ""
	for c in text:
		idx = alphabet(c)
		if idx is not None:
			newIdx = (int(a) * idx + int(b)) % alphabet(None)
			result += alphabet(newIdx)
		else:
			extChars += "'" + c + "', "
			result += c
	if extChars != "":
		print("Invalid characters in plaintext skipped - " + extChars + "- outside of encrypt function available alphabet")
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
		idx = alphabet(c)
		if idx is not None:
			newIdx = ((idx - int(b)) * inv) % alphabet(None)
			result += alphabet(newIdx)
		else:
			result += c
	return result


# Encrypts the given text using an affine cipher in a standard Z_26 alphabet
def encrypt26(text : str, a : int, b : int) -> str:
	return encrypt(text, a, b, alphabet.standard)

# Decrypts the given text using an affine cipher in a standard Z_26 alphabet
def decrypt26(text : str, a : int, b : int) -> str:
	return decrypt(text, a, b, alphabet.standard)

# Encrypts the given text using an affine cipher on an extended character set
def encryptExt(text : str, a : int, b : int) -> str:
	return encrypt(text, a, b, alphabet.extended)

# Decrypts the given text using an affine cipher on an extended character set
def decryptExt(text : str, a : int, b : int) -> str:
	return decrypt(text, a, b, alphabet.extended)


# Alphabet function(s) with the specification expected by the affine_cipher.py program
# Expected specification:
#  - the function takes one argument of variable type and returns a value of variable type
#   - if a whole number (datatype int) is passed to the function, the returned value is the corresponding letter of the given alphabet
#   - if a letter (datatype str) is passed to the function, the returned value is the corresponding numeric position of this letter in the given alphabet
#   - if None is passed to the function, the returned value is the number of characters in the alphabet, or the modulus of the Z_m set to which the positions of the letters are confined

def standard(arg):
	if type(arg) is str:
		return (ord(arg.upper()) - 64) % 26
	elif type(arg) is int:
		return chr((arg if arg > 0 else 26) + 64)
	else:
		return 26

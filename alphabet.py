# Alphabet function(s) with the specification expected by the affine_cipher.py program
# Expected specification:
#  - the function takes one argument of variable type and returns a value of variable type
#   - if a whole number (datatype int) is passed to the function, the returned value is the corresponding letter of the given alphabet
#   - if a letter (datatype str) is passed to the function, the returned value is the corresponding numeric position of this letter in the given alphabet
#   - if None is passed to the function, the returned value is the number of characters in the alphabet, or the modulus of the Z_m set to which the positions of the letters are confined


def _alphabetList(arg, aList):
	if type(arg) is str:
		if arg in aList:
			return aList.index(arg)
	elif type(arg) is int:
		if arg < len(aList):
			return aList[arg]
	else:
		return len(aList)
	# Exit with None if nothing returned previously
	return None



# Standard Z_26 alphabet list with A->1 and Z->0 indexing
_std_list = [
	"Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"
]

# Standard 26-letter A-Z
def standard(arg):
	return _alphabetList(arg, _std_list)

_std_list_2 = [
	"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

def standard2(arg):
	return _alphabetList(arg, _std_list_2)

# Extended alphabet list
_ext_list = _std_list + [
	"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
	"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
	" ", ",", ".", "!", "?", "-", "'", '"'
]

# Extended alphabet consisting of capital and lowercase A-Z, followed by numbers 0-9, space and punctuation marks (,.!?-'")
def extended(arg):
	return _alphabetList(arg, _ext_list)

_27_list = ["!", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def ext27(arg):
	return _alphabetList(arg, _27_list)


_37_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]

def ext37(arg):
	return _alphabetList(arg, _37_list)

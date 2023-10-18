# A demonstration program using the Z_26 affine cipher in the module affine_cipher to encrypt or decrypt user-specified values

import alphabet as a
import affine_cipher as cipher


if __name__ == "__main__":
	print("Affine Cipher System")
	while True:
		op = input("Select operation: [E]ncrypt/[D]ecrypt/[Q]uit: ")
		func = None
		
		# Selecting the function
		if (op.lower())[0] == "e":
			func = cipher.encrypt26
		elif (op.lower())[0] == "d":
			func = cipher.decrypt26
		elif (op.lower())[0] == "q":
			break
		else:
			print("Incorrect operation: " + op + "\n")
			continue

		# Using the function to process given text
		text = input("Enter text to process: ")
		a_key = int(input("Enter the 'a' key of the cipher: "))
		b_key = int(input("Enter the 'b' key of the cipher: "))
		print("Result: " + func(text, a_key, b_key) + "\n")

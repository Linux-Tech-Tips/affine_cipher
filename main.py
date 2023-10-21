# A demonstration program using the Z_26 affine cipher in the module affine_cipher to encrypt or decrypt user-specified values

import alphabet as a
import affine_cipher as cipher


if __name__ == "__main__":
	print("Affine Cipher System")

	encrypt = cipher.encrypt26
	decrypt = cipher.decrypt26

	while True:
		op = input("Select operation (charset " + ("Z_26" if encrypt == cipher.encrypt26 else "extended") + "): [E]ncrypt/[D]ecrypt/[C]harset/[Q]uit: ")
		func = None
		
		# Selecting the function
		if (op.lower())[0] == "e":
			func = encrypt
		elif (op.lower())[0] == "d":
			func = decrypt
		elif (op.lower())[0] == "q":
			break
		elif (op.lower())[0] == "c":
			if encrypt == cipher.encrypt26:
				encrypt = cipher.encryptExt
				decrypt = cipher.decryptExt
				print("Changed character set mode to extended")
			else:
				encrypt = cipher.encrypt26
				decrypt = cipher.decrypt26
				print("Changed character set mode to Z_26")
			continue
		else:
			print("Incorrect operation: " + op + "\n")
			continue

		# Using the function to process given text
		text = input("Enter text to process: ")
		a_key = int(input("Enter the 'a' key of the cipher: "))
		b_key = int(input("Enter the 'b' key of the cipher: "))
		print("Result: " + str(func(text, a_key, b_key)) + "\n")

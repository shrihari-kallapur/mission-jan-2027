passcode = input("Enter your passcode")

has_upper = False
has_lower = False
has_digit = False

for ps in passcode:
	if ps.isupper():
		has_upper = True
	elif ps.islower():
		has_lower = True
	elif ps.isdigit():
		has_digit = True

if has_upper and has_lower and has_digit and len(passcode) >= 8:
	print("Strong Password")
else:
	print("Weak Password")



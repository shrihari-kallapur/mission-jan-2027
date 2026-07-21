budget = int(input("Enter your budget"))

if budget < 50000:
	print("Save more before buying a Jetson board.")
elif 50000 <= budget <= 80000:
	print("Jetson Orin Nano Super Developer Kit")
else:
	print("Consider Jetson Orin NX or higher.")

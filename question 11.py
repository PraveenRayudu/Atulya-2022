original = input("give any word:")

reverse = ""
for i in original:
	reverse = i + reverse

if (original == reverse):
	print("it is pallindrome")
else:
	print("it is not pallindrome")

t = True
while t:
	try:
		exec(input("run code: "))
		t=False
	except (SyntaxError, NameError, AttributeError, ValueError):
		print("error Try again")
print("well done")
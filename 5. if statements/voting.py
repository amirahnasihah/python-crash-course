''' if Statements '''

print("''' Simple if Statements '''\n")

age = 19		# variable as age
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")


print("\n\n''' if-else Statements '''")

age = 17
if age >= 18:		# 17 less than 18
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")


# works bs it only has two possible situations to evaluate:
# either old enough to vote or not old enough.
# if-else structure works in situations to execute one of two possible actions.
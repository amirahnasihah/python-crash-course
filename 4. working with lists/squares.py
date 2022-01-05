# Using range() to Make a List of Numbers
print("Make a list of the first 10 square numbers:")

squares = []		# start at empty list as squares
# To loop through each value from 1 to 10 using range().
for value in range(1, 11):
# Inside the loop, the current value is raised to 
# the second power and assigned to the variable square.
	square = value ** 2 
	squares.append(square) 	
	# each new value of square is 
	# appended to the list squares

print(squares)


# more concise, omit temporarily variable square
print("\nCode more concise, omit variable square:")
squares = []
for value in range(1, 11):
	squares.append(value**2)

print(squares)


# Simple Statistics with a List of Numbers
print("\n\nSimple Statistics:")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Min:")
print(min(digits))

print("Max:")
print(max(digits))

print("Sum:")
print(sum(digits))


# List Comprehensions
# allows to generate same list in just one line of code.
# much better
print("\nList comprehensions: single line code")

squares = [value**2 for value in range(1, 11)]
print(squares)
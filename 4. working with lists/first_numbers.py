''' Making Numerical Lists '''

# range() Function |to print a series of numbers|
print("From 1 to 4:")
for value in range(1, 5):
	print(value) 	# off-by-one behavior >>> 1,2,3,4

print("\nFrom 1 to 5:")
for value in range(1, 6):
	print(value)

print("\nFrom 0 to 5:")
for  value in range(6):
	print(value)





# even_numbers.py

# range() to Make a List of Numbers |convert range() into list()|
# wrap list() around a call to the range() function.
print("\nUse range() into list():")
numbers = list(range(1, 6))
print(numbers)

print("\nUse range() to skip numbers:")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(5, 13, 3))
print(odd_numbers)
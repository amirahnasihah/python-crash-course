''' TUPLES '''
# Tuples create a list of items that cannot change.
# values that cannot change is immutable.
# immutable list is called a tuple.

''' Defining a Tuple '''
# tuple use parentheses, ()
# list use square brackets, []
print("''' Defining a Tuple '''")

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# change one of the items in the tuple.
dimensions = (200, 50)
''' dimensions[0] = 250	'''	# can’t assign new value in tuple


my_t = (3,)
print(my_t[:])


''' Looping Through All Values in a Tuple '''
print("\n''' Looping Through All Values in a Tuple '''")

dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)


''' Writing over a Tuple '''
print("\n''' Writing over a Tuple '''")

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 200)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
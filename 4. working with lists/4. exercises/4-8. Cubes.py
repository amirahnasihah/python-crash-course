''' A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube. '''

# Lists comprehension.
print("My answer: lists comprehension")

cubes = [value**3 for value in range(1, 11)]
print(cubes)

# With variable.
print("\nMy answer: with variable")

numbers = []
for value in range(1, 11):
	number = value ** 3
	numbers.append(number)

for number in numbers:		##### FAHAMKANNN!!!
	print(number)

# Omit variable. | concise |
print("\nMy answer: omit variable")

numbers = []
for value in range(1, 11):
	numbers.append(value**3)

print(numbers)


# Matt answer:
print("\n\nMatt answer:")

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)



''' 
cubes = [] 		# lists bernama cubes
for number in range(1, 11):		# for loop;**
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)


** untuk setiap nombor dalam range 1 hingga 10,
satu variable cube assignkan utk setiap nombor dengan kuasa 3,
lists cubes tambah dengan variable kuasa 3

untuk setiap satu variable cube dalam cubes lists,
print setiap satu variable cube

'''
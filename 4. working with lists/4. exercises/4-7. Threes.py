''' Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list. '''

# Lists comprehension.
print("My answer: lists comprehension")

multiples = [value*3 for value in range(3, 31)]
print(multiples)

# With variable.
print("\nMy answer: with variable")

numbers = []
for value in range(3, 31):
	number = value * 3
	numbers.append(number)

print(numbers)

# Omit variable. | concise |
print("\nMy answer: omit variable")

numbers = []
for value in range(3, 31):
	numbers.append(value*3)

print(numbers)


# Matt answer. | similar as 4-6 |
print("\n\nMatt answer:")

threes = list(range(3, 31, 3))

for number in threes:
    print(number)
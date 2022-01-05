''' 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive. '''

print("My answer:")

twenties = [value for value in range (1, 21)]
print(twenties)


# Answer
print("\nThis is the answer:")

numbers = list(range(1, 21))

for number in numbers:
	print(number)



''' Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window.) '''

#my answer
print("\nMy answer:")

millions = list(range(1, 1_000_001))

for million in millions:
	print(million)
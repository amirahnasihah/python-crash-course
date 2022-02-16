''' Passing an Arbitrary(random) Number of Arguments '''

def make_pizza(*toppings):
	"""Print the list of toppings that have been requested"""
	print(toppings)
	
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# asterisk in parameter name *toppings is to make an empty tuple() called toppings.
# print() call in function body shows Python can handle a function call with one value ('pepperoni') & a call with three values (mushrooms, green ....)
# regardless, it packs arguments into a tuple.


print("\n")
# replace print() call with for loop.

def make_pizza(*toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")
		
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')



print("\n''' Mixing Positional and Arbitrary Arguments '''")

# parameter accepts arbitrary number of arguments must be placed in last function definition.

def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")
		
make_pizza(16, 'pepperoni')
make_pizza(22, 'mushrooms', 'green peppers', 'extra cheese')



''' Storing Your Functions in Modules '''

print("\n\n''' Importing an Entire Module '''")

''' NESTING ''' # IMPORTANT!

print("''' A List in a Dictionary '''\n")

# put a list inside a dictionary

# example: two kinds of information are stored for each
# pizza: a type of crust and a list of toppings

# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

print("\nThis is a very long line "
	"to be tested in python")

# can nest a list inside a dictionary any time you want more than
# one value to be associated with a single key in a dictionary.


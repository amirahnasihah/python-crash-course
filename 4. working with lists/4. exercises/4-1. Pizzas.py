# fav pizzas
# PEP 8 = Python Enhancement Proposal

print("Print my favourite pizzas:")
fav_pizzas = ['cheese', 'pepperoni', 'prawn', 'hawaiian chicken']
for pizza in fav_pizzas:
	print(pizza.title())

print("\nPrint sentence of each pizza:")
fav_pizzas = ['cheese', 'pepperoni', 'prawn', 'hawaiian chicken']
for fav_pizza in fav_pizzas:
	print(f"I like {fav_pizza} pizza.")

print(f"\nI really love pizza!")


# OR ALT ANSWER

favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print(f"I really love {pizza} pizza!")

print("\nI really love pizza!")

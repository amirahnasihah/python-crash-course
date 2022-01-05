''' Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following: '''

# Add new pizza to original list.
fav_pizzas = ['cheese', 'pepperoni', 'prawn', 'hawaiian chicken']
friend_pizzas = fav_pizzas[:]

fav_pizzas.append('meatsaurus')

# Add different pizza to friend
friend_pizzas.append('pinneapple')

# Prove of 2 separate lists.
print("My favourite pizzas are:")
for pizza in fav_pizzas:
	print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())


# Matt answer.
print("\n\n\nMatt answer: at end")

print("My favorite pizzas are:")
for pizza in fav_pizzas:
    print(f"- {pizza.title()}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
''' A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple. '''

foods = ('nasi lemak', 'sandwich', 'juice', 'noodles', 'dessert')
print("Original foods:")
for food in foods:
	print(food.title())


# modify
foods = ('nasi lemak', 'sandwich', 'juice', 'noodles', 'dessert')
print("\nModified foods:")
for food in foods:
	print(food.title())

# foods[0] = ('nasi goreng')
print(foods)


# Changes its menu.
buffets = ('nasi lemak', 'sandwich', 'juice', 'noodles', 'dessert')
print("\nOriginal buffets:")
for buffet in buffets:
	print(buffet.title())

buffets = ('nasi goreng', 'sandwich', 'juice', 'samyang', 'dessert')
print("\nModified buffets:")
for buffet in buffets:
	print(buffet.title())



# MATT ANSWER.
print("\n\n\nMATT ANSWER:")


menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print(f"- {item.title()}")


print("""
Hello, this is a test to write a very long statement.
hdjahjkashi dontknow
""")
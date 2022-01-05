''' All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods. '''

# Copy all my fav to friend's fav
print("Create friend list by copying ours:")

my_foods = ['pizza', 'burger', 'cheese cake']
friend_foods = my_foods[:]

print("My favourite foods are:")
for my_food in my_foods:
	print(f"- {my_food.title()}")

print("\nMy friend's favourite foods are:")
for friend_food in friend_foods:
	print(f"- {friend_food.title()}")


# Prove have 2 separate lists
print("\n\nProve of 2 separate lists:")

my_foods = ['pizza', 'burger', 'cheese cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
for my_food in my_foods:
	print(f"- {my_food.upper()}")

print("\nMy friend's favourite foods are:")
for friend_food in friend_foods:
	print(f"- {friend_food.upper()}")


# Try copy list without using a slice.
print("\n\nTry copy list without using a slice: not work")

my_foods = ['pizza', 'falafel', 'carrot cake']

	# This doesn't work: pg102
friend_foods = my_foods 	#DOES NOT WORK AS COPYING

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for my_food in my_foods:
	print(f"- {my_food.upper()}")

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
	print(f"- {friend_food.upper()}")

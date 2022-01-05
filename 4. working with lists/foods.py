''' Copying a List '''

# Copy all my fav to friend's fav
print("Create friend list by copying ours:")

my_foods = ['pizza', 'burger', 'cheese cake']
friend_foods = my_foods[:]

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

# Prove have 2 separate lists
print("\n\nProve of 2 separate lists:")

my_foods = ['pizza', 'burger', 'cheese cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)


# Try copy list without using a slice.
print("\n\nTry copy list without using a slice: not work")

my_foods = ['pizza', 'falafel', 'carrot cake']

	# This doesn't work: pg102
friend_foods = my_foods		# not copy but set friend_foods equal to my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#make sure you are copying the list using a slice. [:]
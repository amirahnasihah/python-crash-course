''' Working with Part of a List '''

'''Slicing a List. '''
print("Slice with first 3 elements:")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Automatically starts slice at beginning of list.
print("\nOmit first index in a slice:")
print(players[:4])

# All items from the third item through the last item.
print("\nSlice inlcudes the end of list:")
print(players[2:])

# From end of list |negative index returns|
print("\nFrom end of list:")
print(players[-3:])		# last three players



''' Looping Through a Slice. '''

# use a slice in a for loop if you want to loop through a 
# subset of the elements in a list.

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\nHere are the first three players on my team:")
for player in players[:3]:
	print(player.title())

print("\nExperiment with myself: using index on each player")
for player in players[:]:
	print(player[0:3].upper())
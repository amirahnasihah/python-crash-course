''' NESTING ''' # Important!!

# to store multiple dictionaries in a list, or a list of
# items as a value in a dictionary. This called nesting.
# can nest dictionaries inside a list, a list of items inside 
# a dictionary, or even a dictionary inside another dictionary.
# make a list of aliens to manage many aliens.

print("''' A List of Dictionaries '''")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# store dictionaries in a list
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

print("\n")

# more than 3 aliens
# Make an empty list for storing aliens.
aliens = []

# Make 30 aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens. (slice method)
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


# Begins with empty list to hold all aliens that will be created.
# At range() returns a series of numbers, which just tells
# Python how many times we want the loop to repeat. (30 times)
# Each time the loop runs we create a new_alien
# and then append each new alien to the list aliens.
# We use a slice to print the first 5 aliens, and
# then print the length of the list to show all 30 aliens.


print("\n\n")


# to change some aliens color & moving faster as game progresses.

aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

for alien in aliens[:5]:
	print(alien)
print("...")


# Because we want to modify the first three aliens, we loop 
# through a slice that includes only the first three aliens.
# Write an if statement to make sure only modifying green aliens.
# If the alien is green, we change the color, speed, point.

# Could expand this loop by adding an elif block that turns yellow.

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

for alien in aliens[7]:
	print(alien)
print(".....")

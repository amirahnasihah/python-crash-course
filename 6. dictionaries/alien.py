print("''' A Simple Dictionary '''")

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0['color'].upper())


print("\n\n''' Working with Dictionaries '''")

alien_0 = {'color': 'green', 'points': 5} # 2 key-value pairs


print("\n\n''' Accessing Values in a Dictionary '''")

alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['color'].upper())

new_points = alien_0['points']  #value assigned to variable new_points
print(f"\nYou just earned {new_points} points!")


print("\n\n''' Adding New Key-Value Pairs '''")

alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

alien_0['x_position'] = 0 	# add new
alien_0['y_position'] = 25
print(alien_0)	# add new info, & 4 key-value pairs


print("\n\n''' Start with an Empty Dictionary '''")

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


print("\n\n''' Modifying Values in a Dictionary '''")

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


# track position that can move at diff speeds.
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

# move the alien to the right.
# determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# this must be a fast alien.
	x_increment = 3

# the new positin is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


print("\n\n''' Removing Key-Value Pairs (Permanently) '''") 	# del statement

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']		# delete permanently
print(alien_0)
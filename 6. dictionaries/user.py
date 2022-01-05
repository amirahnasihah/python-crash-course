''' Looping Through a Dictionary '''

# can loop through all of a dictionary’s key-value pairs, 
# through its keys, or through its values

print("''' Looping Through All Key-Value Pairs '''")

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

# abbreviations > for k, v in user_0.items():
# method items() = returns a list of key-value pairs.
for key, value in user_0.items():	
	print(f"\nKey: {key}")
	print(f"Value: {value}")


user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

print(f"\n{user_0}")	# this is dictionary with key-value pairs
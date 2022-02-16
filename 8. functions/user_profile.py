''' Passing an Arbitrary(random) Number of Arguments '''

print("''' Using Arbitrary Keyword Arguments '''")


def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first name'] = first
	user_info['last name'] = last
	return user_info
	
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# double asterisk cause to create an empty dictionary called user_info.


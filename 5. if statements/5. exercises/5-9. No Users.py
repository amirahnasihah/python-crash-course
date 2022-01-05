''' Add an if test to hello_admin.py to make sure the list of users is
not empty. '''

usernames = []

if usernames: 		# PERHATI BETUL2!
	for username in usernames:
		if username == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello {username.title()}, thank you for logging in again.")
else:
	print("We need to find some users!")
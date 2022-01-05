''' Do the following to create a program that simulates
how websites ensure that everyone has a unique username '''

current_users = ['seha', 'Hyerim', 'haizum', 'therongaks']
new_users = ['EUNJI', 'hyerim', 'archangel', 'yunho', 'SEHA']

for username in new_users:
	if username in current_users:
		print(f"Username {username.title()} has already been used.")
	else:
		print(f"Username {username.title()} is available.")



# CASE INSENSITIVE
''' If 'John' has been used, 'JOHN' should not be accepted. '''
''' To do this, you’ll need to make a copy of current_users 
containing the lowercase versions of all existing users.'''

print("\n\nWith Case Insensitive:\n")

current_users = ['seha', 'Hyerim', 'haizum', 'therongaks']
new_users = ['EUNJI', 'hyerim', 'archangel', 'yunho', 'SEHA']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(f"Username {new_user} has already been used.")
	else:
		print(f"Username {new_user} is available.")
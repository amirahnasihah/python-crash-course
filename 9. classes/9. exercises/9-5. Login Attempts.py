class User:
	"""Represent a simple user profile."""
    
	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize the user."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()
		self.login_attempts = 0 #default value

	def describe_user(self):
		"""Display a summary of the user's information."""
		print(f"\n{self.first_name} {self.last_name}")
		print(f" Username: {self.username}")
		print(f" Email: {self.email}")
		print(f" Location: {self.location}")

	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print(f"\nWelcome back, {self.username}!")
		
	def increment_login_attempts(self):
		"""Allow user to increment the value of login_attempts by 1."""
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		"""Allow to reset the value of login_attempts to 0"""
		self.login_attempts = 0

antonio = User('antonio', 'vivaldi', '4seasons', 'antonio@example.com', 'italy', )
antonio.describe_user()
antonio.greet_user()

print("\nMaking 3 login attempts...")
antonio.increment_login_attempts()
antonio.increment_login_attempts()
antonio.increment_login_attempts()
print(f"Login attempts: {antonio.login_attempts}")

print("Resetting login attempts...")
antonio.reset_login_attempts()
print(f"Login attempts: {antonio.login_attempts}")
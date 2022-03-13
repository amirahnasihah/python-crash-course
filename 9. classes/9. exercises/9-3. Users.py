class User:
    """A simple attempt to represent a user."""
    
    def __init__(self, first_name, last_name, job):
        """Initialize first name, last name, job."""
        self.first = first_name.title()
        self.last = last_name.title()
        self.job = job
        
    def describe_users(self):
        """Summarize of user's information."""
        msg = f"{self.first} {self.last}"
        print(f"\nName: {msg}, Occupation: {self.job}")
        
    def greet_user(self):
        """Simulate greeting to the user."""
        msg = f"Hi, apa khabar {self.first} {self.last}"
        print(f"{msg}")
        
#instance user called class User
user = User('antonio', 'vivaldi', 'violinist')

#print attributes one-by-one (first, last, job)
print(user.first)
print(user.last)
print(user.job)

#instance user called class User
#calling both methods/functions
user = User('antonio', 'vivaldi', 'violinist')
user.describe_users()
user.greet_user()

user = User('ludwig', 'beethoven', 'pianist')
user.describe_users()
user.greet_user()

user = User('johann', 'strauss', 'composer')
user.describe_users()
user.greet_user()
''' Passing a List '''

# pass a list to a function, whether a list or dictionaries/complex objects.

# example sends a list of names to a function called greet_users():

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
        
# make in lists.
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
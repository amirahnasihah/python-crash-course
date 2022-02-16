''' functions '''

# functions are blocks of code that are designed to do one specific job.
# if need perform task multiple times, call the function dedicated to handling that task.

print("''' Defining a Function '''")

def greet_user():   
    """Display a simple greeting."""   
    print("Hello!")   
    
greet_user()   


print("\n''' Passing Information to a Function '''")

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")
    
greet_user('jesse')



''' Return Values '''

print("\n''' Using a Function with a while Loop '''")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
    
# This is an infinite Loop!
while True:
    print("\nPlease tell me your name? ")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    
# problem with while Loop: need defined 'quit' condition.
# use break statement where user can quit asap, in each input. ↓↓↓

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name? ")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
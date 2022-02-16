def make_shirt(size, text):
    """Summarize of the t-shirt."""
    print(f"\nThis shirt's size is {size}.")
    print(f"The message is printed as {text.upper()}")
    
# positional arguments
make_shirt('small', 'rock oo!')
make_shirt('rock oo!', 'small') #incorrect position

# keyword arguments
make_shirt(size='medium', text='go python!')
make_shirt(text='go python!', size='medium')
''' Nesting '''

print("''' A Dictionary in a Dictionary '''")

# can nest a dictionary inside another dictionary, but 
# code can get complicated quickly when you do.

users = {       # main dict
    'aeinstein': {      # username
        'first': 'albert',      # user_info {}
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    'seha': {
        'first': 'seha',
        'last': 'zily',
        'location': 'kota bharu',
        },

    }

for username, user_info in users.items(): # 1
    print(f"\nUsername: {username}") # 2
    full_name = f"{user_info['first']} {user_info['last']}" # 3
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}") # 4
    print(f"\tLocation: {location.title()}")

''' Explaination '''
# first define a dictionary called users with three keys:
# one each for the usernames 'aeinstein', 'mcurie', 'seha'.

# value associated with each key is a dictionary includes:
# each user’s first name, last name, and location.

# at 1 we use for loop through the users dictionary. 
# Python assigns each key to the variable username, and the 
# dictionary associated with each username is assigned to the
# variable user_info.

# inside the main dictionary loop, we print the username at 2.

# at 3 start accessing the inner dictionary.
# the variable user_info, contains dictionary of user 
# information, has three keys: 'first', 'last', and 'location'.

# we use each key to generate a neatly formatted full
# name and location for each person, and then print a 
# summary of what we know about each user.

# the structure of each user’s dictionary is identical.
# this structure makes nested dictionaries easier to work with.
# If each user’s dictionary had different keys, the code inside the
# for loop would be more complicated.
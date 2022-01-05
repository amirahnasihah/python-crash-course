''' Start with the program you wrote for Exercise 6-1 (page 99). 
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.'''

# A list of dictionaries
# make an empty list to store people in.
people = []

# define some people, and add them to the list.

person = {
    'first_name': 'jeong',
    'last_name': 'eunji',
    'age': 29,
    'city': 'seoul',
    }
people.append(person) # add person dict to people list

person = {
    'first_name': 'park',
    'last_name': 'chorong',
    'age': 32,
    'city': 'gangnam',
    }
people.append(person)

person = {
    'first_name': 'marie',
    'last_name': 'curie',
    'age': 88,
    'city': 'paris',
    }
people.append(person)

# display all the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")
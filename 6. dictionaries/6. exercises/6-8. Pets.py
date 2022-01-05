''' Make several dictionaries, where each dictionary represents a different
pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. '''

# Dictionaries in a List \ A list of dictionaries
# make an empty list to store pets in.
pets = []

# make individual pets, and store each in the list.
pet = {
    'animal type': 'dog',
    'name': 'meong',
    'owner': 'eunji',
    'weight': 36,
    'eats': 'shoes',
    }
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'yuyu',
    'owner': 'yunho',
    'weight': 32,
    'eats': 'sofa'
    }
pets.append(pet)

pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
    }
pets.append(pet)

# display info about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value}")

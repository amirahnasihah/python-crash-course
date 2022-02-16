''' Return Values '''

print("''' Returning a Dictionary {'key': 'value'} '''")
# function can return any kind of value.
# returns a dictionary representing a person.

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('antonio', 'vivaldi')
print(musician)


# can extend this function to accept optional values or extra info that want to store about a person
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('antonio', 'vivaldi', age=27)
print(musician)


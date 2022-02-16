''' Return Values '''

print("''' Returning a Simple Value '''")
# works best with large data.

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('antonio', 'vivaldi')
print(musician)


print("\n''' Making an Argument Optional '''")
# users can choose to provide extra information if want to.

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('antonio', 'lucio', 'vivaldi')
print(musician)


# give argument optional an empty default value.
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('antonio', 'vivaldi')
print(musician)

musician = get_formatted_name('ludwig', 'beethoven', 'van')
print(musician)

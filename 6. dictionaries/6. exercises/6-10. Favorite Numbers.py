''' Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers. '''

favorite_numbers = {
    'mandy': [42, 55],
    'micah': [23, 238908, 23712873],
    'gus': [7, 283981293],
    'hank': [1000_000, 100],
    'maggie': [0, 1, 2, 3],
    }

for key, values in favorite_numbers.items():
    print(f"\n{key.title()}'s favorite numbers are:")
    for value in values:
        print(f"  {value}")

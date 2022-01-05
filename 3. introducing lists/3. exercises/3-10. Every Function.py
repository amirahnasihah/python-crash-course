''' 3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once. '''

cities = ['luxemborg', 'los angeles', 'london', 'seoul', 'new delhi', 'zimbabwe', 'aussie']

# Index positions
print("Print index & case:")
print(cities[3])
print(cities[4].title())
print(f"The country I want to go is {cities[2].upper()}.")


# Change, Add, Append, Insert, del, pop, Remove
print("\nOriginal lists:")
cities = ['luxemborg', 'los angeles', 'london', 'seoul']
print(cities)

print("\nPrint change old element to new element in a lists:")
cities[0] = 'istanbul'
print(cities)

print("\nAdd or append new element to END list:")
cities.append('osaka')
print(cities)

print("\nPrint prove of changes:")
print(cities)

print("\nInsert new element to ANY position list:")
cities.insert(2, 'gwangju')
print(cities)

print("\nRemove permanently ANY element using del statement:")
del cities[2]
print(cities)

print("\nRemove at END & ANY position list to use again using pop():")
popped_cities = cities.pop()
print(cities)
print(popped_cities)
print(cities.pop(0).upper())

print("\nChecking originality:")
print(cities)

print("\nRemove the value without knowing the position:")
cities.append('bandung')
cities.insert(3, 'australia')

cities.remove('los angeles')
print(cities)


# sort() permanently, sorted() temporarily, reverse()
print("\n\n\nOriginal list of sort(), sorted(): ")
cities = ['luxemborg', 'los angeles', 'london', 'seoul', 'new delhi', 'zimbabwe', 'aussie']
print(cities)

# sort()
print("\nUsing sort() permanently:")
cities.sort()
print(cities)

# prove original permanently
print("\nPrint original with permanently change:")
print(cities)

# sort() + reverse
print("\nPrint sort() with reverse permanently:")
cities.sort(reverse=True)
print(cities)

# prove sort() + reverse originality
print("\nPrint original sort() with reverse permanently change:")
print(cities)

# original
print("\nNew orginal no change:")
cities = ['luxemborg', 'los angeles', 'london', 'seoul', 'new delhi', 'zimbabwe', 'aussie']
print(cities)

# temporarily with sorted()
print("\nPrint temporarily with sorted():")
print(sorted(cities))

# prove to temporarily change
print("\nProve to temporarily change:")
print(cities)

# sorted() + reverse()
print("\nPrint sorted() with reverse temporarily:")
print(sorted(cities, reverse=True))

# original
print("\nOriginal:")
print(cities)

# Add, change, delete, remove
''' 3-8. Seeing the World: Think of at least five places in the world you’d like to
visit. '''


# locations
print("Raw locations list in not alphabetical order:")
locations = ['makkah', 'korea', 'japan', 'london', 'switzerland', 'los angeles', 'indonesia']
print(locations)


# sorted()
print("\nsorted() in alphabetical order:")
print(sorted(locations))


# locations
print("\nProve in its original:")
print(locations)


# sorted() + reverse()
print("\nsorted() in reverse alphabetical order:")

print(sorted(locations, reverse=True))


# locations
print("\nProve in its original again:")
print(locations)


# reverse() again
print("\nreverse() again:")
locations.reverse()
print(locations)


# sort() alphabeticallly
print("\nUse sort() alphabetically:")
locations.sort()
print(locations)


# sort() + reverse()
print("\nUse sort() with reverse alphabetically:")
locations.sort(reverse=True)
print(locations)




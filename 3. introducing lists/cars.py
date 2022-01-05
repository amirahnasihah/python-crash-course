''' Organizing a List, pg81'''

# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)		# sort/store alphabetically permanently


# sort() + reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)		# in reverse alphabetically permanent


# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))			# sorted(lists_name) function

print("\nHere is the original list again:")
print(cars)

print("\nHere is the sorted list in reverse argument:")
cars.reverse()
print(cars)		# reverses the order of list not alphabetically
print('\n')


# Print a List in reverse() Order not alphabetically >> method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()		# lists_name.reverse()
print(cars)		# permanently change


# sorted() + reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nsorted() in reverse alphabetical order:")

print(sorted(cars, reverse=True))


# Finding the Length of a List >>> len() = number of items
''' len() it starts count at 1 not 0 '''
cars = ['bmw', 'audi', 'toyota', 'subaru', 'mercedes']
print(len(cars))
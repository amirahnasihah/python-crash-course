# c3; pg74
# Changing, Adding, and Removing Elements


# Modifying Elements in a List
''' syntax for modifying an element = to syntax for 
accessing an element in a list. To change an element; 
list_name followed by index of the element that want to change, and then give
the new value you want that item to have. '''
motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

motorcyles[0] = 'ducati'
print(motorcyles)			#changed/replace element in list
print('\n')



# Adding Elements to a List

# Appending Elements to the End of a List >>> append() method
motorcyles = ['honda', 'yamaha', 'suzuki']

motorcyles.append('ducati')
print(motorcyles)

# append() method
print('\n#start with an empty list:')

motorcyles = []

motorcyles.append('honda')
motorcyles.append('yamaha')
motorcyles.append('suzuki')

print(motorcyles)


# Inserting Elements into a List >>> insert() function
''' add a new element at any position in your list '''
motorcyles = ['honda', 'sym', 'suzuki', 'yamaha']
motorcyles.insert(0, 'ducati')
motorcyles.insert(2, 'insert method at 2')
print(f"\n#Insert method:\n{motorcyles}\n")



# Removing Elements from a List

# Removing an Item Using the del Statement >>> del Statement
''' know the position of the item you want to remove from a list,
can use del statement (permanent remove)'''
motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

del motorcyles[0]
print(motorcyles)


# can no longer access the value that was removed
# from the list after the del statement is used.
print('\nDEL STATEMENT')
motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

del motorcyles[1]
del motorcyles[0]
print(motorcyles)
print('\n')


# Removing an Item >>> pop() Method (end of list)
''' removes the last item in a list, but it lets you work
with that item after removing it.
each time you use pop(), the item you work with is no
longer stored in the list. '''

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcyle = motorcycles.pop()	# pop value from list & store it in variable
print(motorcyles)		# ['honda', 'yamaha']
print(popped_motorcyle)


''' list are stored in chronological order. use pop() '''
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcyle I owned was a {last_owned.title()}.\n")



# Popping Items from any Position in a List
''' each time you use pop(), the item you work with is no
longer stored in the list. '''
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The firt motorcycle I owned was a {first_owned.title()}.\n")


''' del statement or the pop() method,
when want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an
item as you remove it, use the pop() method. '''



# Removing an Item by Value >>> remove() method
''' won’t know the position of the value you want to remove
from a list. '''
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


''' remove() method to work with a value that’s being
removed from a list. '''
print('\n')

motorcyles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcyles)

too_expensive = 'ducati'
motorcyles.remove(too_expensive)	 
# use variable too_expensive to tell which value to remove from list
print(motorcyles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# remove() method deletes only the first occurrence
# use loop to remove all occurrences

''' The remove() method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop
to make sure all occurrences of the value are removed. You’ll learn how to do this in
Chapter 7. '''


''' Avoiding Index Errors When Working with Lists '''

print("\n\nAvoiding Index Errors When Working with Lists:")
motorcyles = ['honda', 'yamaha', 'suzuki', 'modenas']
print(motorcyles[-1])

''' If an index error occurs and you can’t figure out how to resolve it, try printing your
list or just printing the length of your list. '''
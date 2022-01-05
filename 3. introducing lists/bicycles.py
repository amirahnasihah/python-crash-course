''' Lists allow you to store
sets of information in one place, whether you
have just a few items or millions of items.

A list is a collection of items in a particular order. You can make a list that
includes the letters of the alphabet, the digits from 0–9, or the names of
all the people in your family. You can put anything you want into a list, and
the items in your list. usually contains more than one element, it’s a good idea to make the
name of your list plural, such as letters, digits, or names.
'''

# lists start index[] with zero
# len() start counting at one
# lists = use plural 's'
# variable = singular no 's'


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


# accessing elements in a list
''' Lists are ordered collections, so you can access any element in a list by
telling Python the position, or index, of the item desired. '''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("\n" + bicycles[0])
print(bicycles[1].title())


name = "nasihah"
message = "my name is"
print(f"\n{message} {name}")
print("my name is " + name + '\n')
#concatenate(plus sign) (rapatkan 2 string. diff than f-string)
#can only concatenate list (not "str") to list


# Index Positions Start at 0, Not 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3].upper() + '\n')


''' asking for the last element in a list at index -1,
always returns the last item in the list: '''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3] + "\n")


# Using Individual Values from a List
''' can use individual values from a list just as you would any other variable.
For example, you can use f-strings to create a message based on a
value from a list. '''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
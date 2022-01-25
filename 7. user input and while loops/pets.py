''' Using a while Loop with Lists and Dictionaries '''

print("''' Removing All Instances of Specific Values from a List '''")

# remove() function worked bcs value appeared only once in list.
# using while loop can remove all instances of repeated value.

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)
# c3; pg74 try it yourself

# 3-1. names: 
''' Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time. '''
names = ['eunji', 'fina', 'sab', 'dini']
print(names[0])
print(names[1])
print(names[2])
print(names[3] + '\n')


# 3-2. Greetings: 
''' Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message
should be the same, but each message should be personalized with the
person’s name.'''
names = ['eunji', 'fina', 'sab', 'dini']
message = "Thank you for being born,"
print(f"{message} {names[0].title()}!")
print(f"Thank you for being born, {names[1].title()}!")
print(f"Thank you for being born, {names[2].title()}!")
print(f"Thank you for being born, {names[3].title()}!\n")


# 3-3. Your Own List: 
''' Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.” '''
mode_examples = ['honda', 'toyota', 'mazda', 'kriss', 'mercedes']
fav_modes = ['motorcyle', 'car']
print(f"I would like to own a {mode_examples[3].title()} {fav_modes[0]}.")
print(f"I would like to own a {mode_examples[4].title()} {fav_modes[1]}.")

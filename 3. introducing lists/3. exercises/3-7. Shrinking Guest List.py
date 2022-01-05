# 3-7: OR alt answer

# Invite some people to dinner.
guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'gary snyder')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)





print('\n')




#3-7. Shrinking Guest List:
''' new dinner table won’t arrive in time for the dinner, 
and you have space for only two guests. '''


# Start with your program from Exercise 3-6. 
guests = ['seha', 'eunji', 'miru']

print(f"You are invited to dinner tonight at my house, {guests[0].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[1].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[2].title()}.\n")

''' cant make it '''
print(f"\nOhmy, {guests[2].title()} cant make it to dinner.")

''' replace old to new guest '''
guests[2] = 'shane'

''' print new invitation '''
print(f"\nYou are invited to dinner tonight at my house, {guests[0].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[1].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[2].title()}.")

# Add a print() call to the end of program informing that found a bigger dinner table
print("\nWe found a bigger table, lets invite more!")

# Use insert() to add one new guest to the beginning of your list.
guests.insert(0, 'kobayashi')

# Use insert() to add one new guest to the middle of your list.
guests.insert(2, 'tohru')

# Use append() to add one new guest to the end of your list.
guests.append('kanna')

# Print a new set of invitation messages, one for each person.
print(f"You are invited to dinner tonight at my house, {guests[0].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[1].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[2].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[3].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[4].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[5].title()}.")

# Add a new line that prints a message saying that can invite only two people for dinner.

print("\nSorry, I can invite only two people only.")


name = guests.pop()		# at end of list
print(f"Sorry, {name.title()} cant invite you to dinner.")

name = guests.pop()		# at end of list
print(f"Sorry, {name.title()} cant invite you to dinner.")

name = guests.pop(2)		# at any of list
print(f"Sorry, {name.title()} cant invite you to dinner.")

name = guests.pop(0)		# at any of list
print(f"Sorry, {name.title()} cant invite you to dinner.")


# Still invited (seha , eunji)
name = guests[0]
print(f"\n{name.title()}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.\n")

# empty list >>> del() statement
del(guests[0])
del(guests[0])		# zero !!!!

# prove of empty list
print(guests)
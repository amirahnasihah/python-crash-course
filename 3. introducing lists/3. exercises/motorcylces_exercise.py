# c3; pg 80 try it yourself


#3-4. Guest List: 
'''If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner. '''
guests = ['seha', 'eunji', 'miru']

print(f"You are invited to dinner tonight at my house, {guests[0].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[1].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[2].title()}.\n")


# OR ehmatthes.github.io answer:

guests = ['seha', 'eunji', 'miru']

name = guests[0].title()
print(f"I welcome you my dear {name} to my house for dinner.")

name = guests[1].title()
print(f"I welcome you my dear {name} to my house for dinner.")

name = guests[2].title()
print(f"I welcome you my dear {name} to my house for dinner.\n")


#3-5. Changing Guest List: 
''' You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list. '''
guests = ['seha', 'eunji', 'miru']


print(f"You are invited to dinner tonight at my house, {guests[0].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[1].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[2].title()}.")

print(f"\nOhmy, {guests[2].title()} cant make it to dinner.")

# replace old to new guest
guests[2] = 'shane'

# print new invitation
print(f"\nYou are invited to dinner tonight at my house, {guests[0].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[1].title()}.")
print(f"You are invited to dinner tonight at my house, {guests[2].title()}.")



# OR 


# Invite some people to dinner.
guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])						# del statement!!
guests.insert(1, 'gary snyder')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")


#3-6. More Guests: 
''' You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner. '''

# Start with your program from Exercise 3-4 or Exercise 3-5. 
guests = ['seha', 'eunji', 'miru']
del(guests[2])
guests.insert(2, 'shane')

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


print("\n## OR ALT ANSWER\n")

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
print(f"{name}, please come to dinner.\n")



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
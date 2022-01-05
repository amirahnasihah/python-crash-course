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
print(f"{name}, please come to dinner.")
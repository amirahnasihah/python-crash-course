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
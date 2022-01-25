''' Using a while Loop with Lists and Dictionaries '''

# for loop is effective for looping through a list, but shouldn’t modify a list inside a for loop because have trouble keeping track of the items in the list. 
# To modify a list, use a while loop. Using while loops with lists and dictionaries allows to collect, store, and organize lots of input to examine and report on later.

print("''' Moving Items from One List to Another '''")


# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']   #1
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:  #2 
    current_user = unconfirmed_users.pop()  #3
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)    #4
    
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
# at 1, start with unconfirmed_users list & empty list to hold confirmed_users.
# at 2, while loop run as long as list unconfirmed_users not empty.
# at 3, within this loop the pop() function removes unverified users one at a time from the end of unconfirmed_users.
# at 4, Candace is last in unconfirmed_users list, she the first to be removed, assigned to current_user & added to confirmed_users list. Next, brian then alice.
# when list unconfirmed_users empty, loop stops & list confirmed_users is printed.
# polls program using dictionary {name: place}
responses_place = {}

# set a flag to show that polling is active
polling_active = True

while polling_active:
    # Prompt or ask users.
    name = input("\nWhat is your name? ")
    place = input("\nIf you could visit one place in the world, where would you go? ")
    
    # Store place response/infos in dictionary.
    responses_place[name] = place
    
    # Anyone else is going to take the poll too?
    repeat = input("Let other person respond too? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
# Polling is complete. Shown results.
print("\n--- Poll Results ---")
for name, place in responses_place.items():
    print(f"{name.title()} would like to visit {place.title()} once someday. ")
''' Using a while Loop with Lists and Dictionaries '''

print("''' Filling a Dictionary with User Input '''")

# store data collected in a dictionary bcs want to connect each response with certain user.

responses = {}

# set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.    #1
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response in dictionary.     #2
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.    #3
    repeat = input("Would ypu like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
# Polling is complete. Show the results.    #4
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
    
# As long as polling_active is True, code runs in the while loop.
# at 1, Within the loop, the user is prompted to enter name and mountain want to climb.
# at 2, That information is stored in the responses dictionary, and
# at 3, the user is asked whether or not to keep the poll running. If they enter yes, the program enters the while loop again. If no, polling_active flag is set to False, the while loop stops running, and 
# at 4, final code block at displays the result.


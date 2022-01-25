''' Introducing while Loops '''

print("''' Using break to Exit a Loop '''")

# To exit a while loop immediately without running any remaining code in the loop, regardless of any conditional test, use the break statement.

# can stop the while loop in this program by calling break as soon as the user enters the 'quit' value:

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: #1
    city = input(prompt)
    
    if city == 'quit':
        break
else:
    print(f"I'd love to go to {city.title()}!")
    
# at 1, loop that starts with while True will run forever unless it reaches a break statement. The loop in this program continues asking the user to enter the names of cities they’ve been to until they enter 'quit'. When they enter 'quit', the break statement runs, causing Python to exit the loop.
# can use the break statement in any of Python’s loops.


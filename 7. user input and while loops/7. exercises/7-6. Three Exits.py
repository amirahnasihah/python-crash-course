''' Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value. '''

instruction = "\nWhat toppings do you like?"
instruction += "\nEnter 'quit' when finished. "

while True:
    topping = input(instruction)
    if topping == 'quit':
        break
    else:
        print(f"Your desired {topping} have been added!")
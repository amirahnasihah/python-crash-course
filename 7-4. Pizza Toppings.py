''' Write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value. As they enter each topping, print a message saying you’ll add that topping to their pizza. '''

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)   
    if topping != 'quit':
        print(f"You've added {topping} as your topping on pizza!")
    else:
        break
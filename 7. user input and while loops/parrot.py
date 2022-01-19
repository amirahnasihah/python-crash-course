''' How the input() Function Works '''

# input() function pauses your program and waits for 
# the user to enter some text.

# input() function takes one argument: 
# prompt, or instructions, that we want to display to the 
# user so they know what to do

message = input("Tell me something, and I will repeat it back to you: ")
print(message)



''' Introducing while Loops '''

# while loop run as long as a certain condition is true.

print("\n''' Letting the User Choose When to Quit ''' ")

# define a quit value & then keep program running as long as the user not entered the quit value.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    

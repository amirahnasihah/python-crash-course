''' How the input() Function Works '''

# input() function pauses your program and waits for 
# the user to enter some text.

# input() function takes one argument: 
# prompt, or instructions, that we want to display to the 
# user so they know what to do

from prompt_toolkit import prompt

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


''' Introducing while Loops '''

# while loop run as long as a certain condition is true.

print("\n''' Letting the User Choose When to Quit '''")

# define a quit value and then keep the program running as # long as the user has not entered the quit value.

prompt = "\nTell me something, and I will repeat it back to you:"   #1
prompt += "\nEnter 'quit' to end the program. "

message = ""    #2
while message != 'quit':    #3
    message = input(prompt)
    print(message)
    
# Explaination:
# at 1, define a prompt to tells the user their two options: entering a message or entering the quit value.
# at 2, set up a variable message to keep track of whatever value the user enters. 
# define message as an empty string, "", so Python has something to check the first time it reaches the while line. 
# the first time the program runs and Python reaches the while statement, it needs to compare the value of message to 'quit', but no user input has been entered yet.
# If Python has nothing to compare, it won’t be able to continue running the program. To solve this problem, we make sure to give message an initial value. Although it’s just an empty string, it will make sense to Python and allow it to perform the comparison that makes the while loop work.
# at 3, while loop runs as long as the value of message is not 'quit'.
# The first time through the loop, message is just an empty string, so Python enters the loop. At message = input(prompt), Python displays the prompt and waits for the user to enter their input. Whatever they enter is assigned to message and printed; then, Python reevaluates the condition in the while statement. As long as the user has not entered the word 'quit', the prompt is displayed again and Python waits for more input. When the user finally enters 'quit', Python stops executing the while loop and the program ends.


# This program works well, except that it prints the word 'quit' as if it were an actual message. A simple if test fixes this:

prompt = "\nTell me something, and I will repeat it back to you:"   #1
prompt += "\nEnter 'quit' to end the program. "

message = ""    #2
while message != 'quit':    #3
    message = input(prompt)
    if message != 'quit':
        print(message)
        


''' Introducing while Loops '''

print("\n''' Using a Flag '''")

# many different events could cause the program to stop running.
# a flag, acts as a signal to the program. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False.
# As a result, our overall while statement needs to check only one condition: whether or not the flag is currently True.

# flag called active (can call it anything) will monitor whether or not the program should continue running.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True   #1
while active:   #2
    message = input(prompt)
    
    if message == 'quit':   #3
        active = False
    else:   #4
        print(message)
        
# Explaination:
# at 1, set the variable active to True so the program starts in an active state. It makes the while statement simpler because no comparison is made in the while statement itself; the logic is taken care of in other parts of the program.
# at 2, loop continue running as long as the active variable remains True. In the if statement inside the while loop, we check the value of message once the user enters their input.
# at 3, if the user enters 'quit', we set active to False, and the while loop stops.
# at 4, print their input as a message.

# This program has the same output as the previous example where we placed the conditional test directly in the while statement. 
# But now have a flag to indicate whether the overall program is in an active state, it would be easy to add more tests (such as elif statements) for events that should cause active to become False. 
# useful in complicated programs like games in which there may be many events that should each make the program stop running. When any of these events causes the active flag to become False, the main game loop will exit, a Game Over message can be displayed, and the player can be given the option to play again.

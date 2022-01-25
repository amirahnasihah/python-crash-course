''' Introducing while Loops '''

# while loop run as long as a certain condition is true.

print("''' The while Loop in Action '''")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# start to count from 1 by assigning current_number the value 1
# while loop keep running as long as the value of current_number is less than or equal to 5. 
# code inside the loop prints the value of current_number and then adds 1 to that value with current_number += 1.
# Python repeats the loop as long as the condition current_number <= 5 is true. Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2.
# Because 2 is less than 5, Python prints 2 and adds 1 again, making the current number 3, and so on. 
# Once the value is greater than 5, the loop stops running.


print("\n''' Using continue in a Loop '''")

# use the continue statement to return to the beginning of the loop based on the result of a conditional test.

current_number = 0
while current_number < 10:
    current_number += 1     #1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
    
# First set current_number to 0. Because it’s less than 10, Python enters the while loop. at 1, once inside the loop, increment the count by 1, so current_number is 1.
# the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number.


print("\n''' Avoiding Infinite Loops '''")

x = 1
while x <= 5:
    print(x)
    x += 1

#if accidentally omit the line x += 1, the loop will run forever.

# This loop runs forever
'''
x = 1
while x <= 5:
    print(x)
    '''
# Try clicking in the output area of the editor before pressing ctrl-C, and able to cancel an infinite loop. or just close the terminal window.

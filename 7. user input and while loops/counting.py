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
''' Reading from a File '''

print("''' Working with a File’s Contents '''")

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''  # create variable pi_string to hold digits if pi
for line in lines:  # create loop that adds each line of digits to pi_string
    pi_string += line.rstrip()  # and removes newline char from each line
    
print(pi_string)    #print string
print(len(pi_string))   #print also how long the string

print('\nRemoving Whitespace with strip():')

pi_string = ''
for line in lines:
    pi_string += line.strip()   # has whitespace on the left side of the digits in each line, but get rid of by using strip()
    
print(pi_string)
print(len(pi_string))   # string containing pi to 30 decimal places. The string is 32 characters long bcs includes the leading 3 and a decimal point.



print("\n''' Is Your Birthday Contained in Pi? '''")

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
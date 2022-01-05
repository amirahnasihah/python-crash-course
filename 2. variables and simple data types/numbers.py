''' used quite often in programming to keep score in games,
represent data in visualizations, store information in web applications,
and so on. '''

# integers (whole number)
''' (add (+), subtract (-), multiply (*), and divide (/) integers) '''
print(2 + 3)
print(5 - 3)
print(9 * 3)
print(3 / 2)
print("\n")

''' two multiplication symbols to represent exponents: '''
print(3 ** 2)		# power of 3x3
print(3 ** 3)		# 3x3x3


''' order of operations '''
print("\n")
print(2 + 3*4)
print((2 + 3) * 4)



# floats (any number with a decimal point)
print("\n")
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
''' But be aware that you can sometimes get an arbitrary number of decimal
places in your answer:
Just ignore the extra decimal places for now '''
print(0.2 + 0.1)		#0.30000000000000004
print(3 * 0.1)
print("\n")


# integers and floats
''' divide any two numbers, even if they are integers that result in a
whole number, you’ll always get a float: '''
print(4/2)
''' Python defaults to a float in any operation that uses a float, even if the
output is a whole number. '''
print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2)



# underscores in numbers
''' writing long numbers, you can group digits using underscores
to make large numbers more readable: '''
universe_age = 14_000_000_000
print(f"{universe_age}\n")



# multiple assignment
''' assign values to more than one variable using just a single line. 
use this technique most often when initializing a set of numbers.'''
x, y, z = 0, 0, 0
print(x)
print(y)
print(z)

seha, eunji, yunho = 55, 188, 233
print(seha)
print(eunji)
print(f"{yunho}\n")


# constants
''' like a variable whose value stays the same throughout the life
of a program. 
use all capital letters to indicate a variable should be treated as a
constant and never be changed: '''
MAX_CONNECTIONS = 5_000
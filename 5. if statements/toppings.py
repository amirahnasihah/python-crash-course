'''if Statements '''

print("''' Checking for Equality '''")

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!!!")


'''
if statement compares value of requested_topping to value
'anchovies'. If these two values do not match, Python returns True and executes
the code following the if statement. If the two values match, Python
returns False and does not run the code following the if statement.
Because the value of requested_topping is not 'anchovies', the print()
function is executed.
'''


print("\n\n''' Testing Multiple Conditions '''")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

# if-elif-else chain only for one test to pass.
# if statements to check all conditions.


''' Using if Statements with Lists '''

print("\n\n''' Checking for Special Items '''")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")



print("\n\n''' Checking that a list is not empty '''")

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza.")
else:
	print("Are you sure you want a plain pizza?")


print("\n\n'''Using Multiple Lists '''")

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pinneapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping.upper()}")
	else:
		print(f"Sorry, we dont have {requested_topping.upper()}")

print("\nFinished making your pizza!")	
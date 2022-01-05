''' if Statement '''

print("''' The if-elif-else Chain '''\n")

# to determine person's admisission fee.
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")


# more precise to set just price
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f"Your admission cost is ${price}.")

# revised code is easier to modify than the original one.
# just change only one print() call 
# rather than 3 separate calls.


print("\n\n''' Using Multiple elif Blocks '''")

age = 58

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f"Your admission cost	is ${price}.")


print("\n\n''' Omitting the else Block '''")

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >=65:		# elif
	price = 20

print(f"Your admission cost is ${price}.")

# bit clearer than the general else block.
# every block must pass a specific test to be executed.
# else block is a catchall statement.
# can sometimes include invalid or malicious data.
# consider using a final elif block and omit the else block
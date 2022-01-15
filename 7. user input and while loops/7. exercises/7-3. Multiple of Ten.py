''' "Ask the user for a number, and then report whether the number is a multiple of 10 or not. '''

number = input("Give me a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

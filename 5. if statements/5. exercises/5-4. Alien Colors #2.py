''' Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain. '''

print("My answer:")

# else block
alien_color = ['green', 'yellow', 'red']

if alien_color == 'green':
	points = 5
else:
	points = 10

print(f"You just earned {points}!")

# if block

if alien_color == 'green':		# if dengan in je jadi
	points = 5 					# utk check all test
if alien_color == 'red':
	points = 10

print(f"You just earned {points}!")


# SALAHHHHH AHHHAHAH

print("\n\nMatt answer:")

# if block runs:
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")


# else block runs:
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
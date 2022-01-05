''' an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.) '''

# keyword: variable & ASSIGN VALUE OF 'green'

print("My answer:")

alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
	print("You earned 5 points!")
if 'black' in alien_color:
	print("You earned 10 points!")

# matth answer

print("\nMatt answer:")

alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points!")


alien_color = 'red'

if alien_color == 'green':
	print("You just earned 5 points!")
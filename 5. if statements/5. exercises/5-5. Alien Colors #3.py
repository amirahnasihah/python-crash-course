''' if-else chain into if-elif-else chain '''

print("My answer:")

alien_color = 'green'

if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
else:
	points = 15

print(f"You just earned {points}!")


# Matt answer
print("\n\nMatt answer:")

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
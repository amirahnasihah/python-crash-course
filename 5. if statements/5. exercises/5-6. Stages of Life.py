''' if-elif-else chain to determine person's life stage. '''

print("My answer:")


age = 24

if age < 2:
	print("You still a baby.")
elif age < 4:
	print("toddler.")
elif age < 13:
	print("kid.")
elif age < 20:
	print("teenager.")
elif age < 65:
	print("adult.")
else:
	print("elder.")


# Matt answer

print("\n\nMatt answer:")

age = 17

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")
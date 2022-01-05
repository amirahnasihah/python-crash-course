''' Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3. '''

print("My answer:")

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal_number in ordinal_numbers:
	if ordinal_number == 1:
		print("1st")
	elif ordinal_number == 2:
		print("\n2nd")
	elif ordinal_number == 3:
		print("\n3rd")
	else:
		print(f"\n{ordinal_number}th")


# Matt Answer

print("\n\nMatt answer:")

numbers = list(range(1,10))		# list(range(1, 10)) INGATTTTT lagi mudah

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
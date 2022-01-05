''' Use the code in favorite_languages.py (page 97). '''

favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for people, language in favourite_languages.items():
	print(f"{people.title()}'s favorite language is {language.title()}.")


print("\n")


# lists
coders = ['jen', 'sarah', 'edward', 'phil', 'seha', 'eunji', 'yunho']

print('This are the people who should take the poll:')
for coder in coders:
	if coder in favourite_languages.keys():
		print(f"\tThank you for taking the poll, {coder.title()}.")
	else:
		print(f"\t{coder.title()}, what's your favourite programming language?")		
print("''' A Dictionary of Similar Objects '''")

favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',		# add coma, at end much better
	}

language = favourite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")


print("\n\n\n''' Looping Through All Key-Value Pairs '''") # items()

# use method items()
favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',		# add coma, at end much better
	}


for name, language in favourite_languages.items():
	print(f"\nName/Key: {name.upper()}")
	print(f"Language/Value: {language.title()}")
	print(f"\t{name.title()}'s favorite language is {language.title()}.")


print("\n\n''' Looping Through All the Keys in a Dictionary '''") # keys()

# use method keys()
# same as >> for name in favorite_languages:
for name in favourite_languages.keys():
	print(name.title())

print('\n')

# to see name matches in dictionary
favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

friends = ['phil', 'sarah']		# list wanted to print a message to
for name in favourite_languages.keys():
	print(name.title())		# inside loop, print each name

	if name in friends:		# check whether name is in list friends
		language = favourite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}.")
# Everyone’s name is printed, but our friends receive a special message.


print('\n')

favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

# use keys() method to find out a particular person.
if 'erin' not in favourite_languages.keys():
	print("Erin, please take our poll!")



print("\n\n''' Looping Through a Dictionary’s Keys in a Particular Order '''") # sorted() function

favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

# sorted(x.method())

# use sorted() function.
# wrapped the sorted() function around the dictionary.keys() method.
for name in sorted(favourite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")


print("\n\n''' Looping Through All Values in a Dictionary '''") # values() method

favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

# pulls all values without checking for repeats.
print("The following languages have been mentioned:")
for language in favourite_languages.values():
	print(language.title())



# set(x.method())

# A set is a collection in which each item must be unique (No repetitive)
# Can build a set directly using braces and separating the elements with commas
print("\nThe following languages have been mentioned (unique):")
for language in set(favourite_languages.values()):
	print(language.title())



# It’s easy to mistake sets for dictionaries because they’re 
# both wrapped in braces. When you see braces but no key-value 
# pairs, you’re probably looking at a set. Unlike lists and 
# dictionaries, sets do not retain items in any specific order.
languages = {'python', 'ruby', 'python', 'javascript'}
print(languages)	# this is a set no key-value pairs


''' Nesting '''

print("\n\n\n''' A List in a Dictionary '''")

favorite_languages = {
	'jen': ['python', 'ruby'], # value is now a list
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t-{language.title()}")

# should not nest lists and dictionaries too deeply.

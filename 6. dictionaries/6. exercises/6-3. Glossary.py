''' A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary. '''

print("My answer:")

words = {
	'string': 'sentences',
	'float': 'a decimal number',
	'dictionary': 'to store a piece of info',
	'integer': 'a whole number',
	'tuples': 'a lists that cannot be changed ()'
	}

word = 'string'.title()
print(f"{word}: {words['string']}")

word = 'float'
print(f"\n{word.title()}: {words['float']}")

word = 'dictionary'
print(f"\n{word.title()}: {words['dictionary']}")

word = 'integer'
print(f"\n{word.title()}: {words['integer']}")

word = 'tuples'
print(f"\n{word.title()}: {words['tuples']}")



# Matt answer

print("\n\n\nMatt answer:")


glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order. []',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs. {}",
    }

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")
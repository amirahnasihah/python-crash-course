print("Looping Through an Entire List:")

print("\nfor loop to print out each name in list:")
magicians = ['eunji', 'seha', 'yunho', 'isaac']
for magician in magicians:
	print(magician)

print("\tread the code as “For every magician in the list of magicians, print the magician’s name.”")
''' read the code as “For every magician in the list of magicians, print the magician’s
name.” '''


# Doing More Work Within a for Loop (indent)
print("\nPrint message to each magician + indented:")

magicians = ['eunji', 'seha', 'yunho', 'isaac']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I cant wait to see your next trick, {magician.title()}.\n")

print(f"Thank you, everyone. That was a great magic show!")

# Avoiding Indentation Errors (logical error)
print("\nForgetting to indent:")
magicians = ['eunji', 'seha', 'yunho', 'isaac']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
print(f"I cant wait to see your next trick, {magician.title()}.\n")

print("Forgetting to Indent Additional Lines is logical error.")
''' syntax is valid Python code, but the code does
not produce the desired result because a problem occurs in its logic. '''

# Indenting Unnecessarily After the Loop (logical error)
print("\nIndenting Unnecessarily After the Loop:")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
	
	print("Thank you everyone, that was a great magic show!") #unnecessary

# Forgetting the Colon (syntax error)
print("\nForgetting the Colon:")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.upper())
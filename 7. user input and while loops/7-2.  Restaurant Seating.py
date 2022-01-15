''' how many people in dinner group '''

prompt = "How many people are in for dinner group? "

people = input(prompt)
people = int(people)

if people > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
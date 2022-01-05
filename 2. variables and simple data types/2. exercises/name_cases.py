# c2; pg63 = try it yourself

# fstring = f""

# 2-3. personal message:
''' Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?” '''
name = "nor amirah nasihah"
message = f"Hello {name}, would you like to learn some Python today?\n"
print(message)


#2-4: name cases:
''' Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case. '''
name = "nor amirah nasihah"
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)

message = f"Hello {name.lower()}, would you like to learn some Python today?"
print(message)

message = f"Hello {name.upper()}, would you like to learn some Python today?"
print(message)


# 2-5. famous quote: 
''' Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks: '''

print('\nAlbert Einstein once said, "A person who never made a mistake never tried anything new."')
print("Albert Einstein once said, “A person who never made a mistake never tried anything new.”")

# 2-6. famous quote 2:
''' Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose
your message and represent it with a new variable called message. Print your
message. '''
famous_person = "albert einstein"
quote = '“A person who never made a mistake never tried anything new.”'
print(f"\n{famous_person.title()} once said, {quote}")


# 2-7. stripping name:
''' Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip(). '''
name = " jeong eunji "		#double method used; title().strip()
print(f"\n{name.title().strip()} is:\n\tActress\n\tApink member\n\tDJ")
print(name.rstrip())
print(name.lstrip())
print(f"{name.strip()}\n")


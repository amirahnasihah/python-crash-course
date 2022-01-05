first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"		#f-strings
print(full_name)		#o: ada lovelace

#Using Variables in Strings
#want two variables to represent a first name and a last name respectively, and then want to combine those values
#To insert a variable’s value into a string, place the letter f immediately before the opening quotation mark
#gabung 2 variables kepada 1 ayat guna f-strings (f = format). Curly braces


#use f-strings to compose complete messages using the information associated with a variable, as shown here:

first_name = "nor amirah"
last_name = "nasihah"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


#use f-strings to compose a message, and then assign the entire message to a variable

first_name = "jeong"
last_name = "eunji"
full_name = f"{first_name} {last_name}"
message = f"Ohayo, {full_name.title()}!"
print(message)

#This code displays the message Ohayo, Jeong Eunji! as well, but by assigning the message to a variable we make the final print() call much simpler


#Adding Whitespace to Strings with Tabs or Newlines

print("python")

#To add a tab to text, use character combination \t:
print("\tPython")


#To add a newline in a string, use the character combination \n:
print("\nPython")

#combine tabs & newlines in a single string.
print("Languages:\n\tPython\n\tC\n\tJavaScript")



#Stripping Whitespace
#Extra whitespace can be confusing in your programs.'python' and 'python ', are two different strings. Python detects the extra space.
# rstrip() method = ensure that no whitespace exists at the right end of a string

favourite_language = 'python '
print(favourite_language)

print(favourite_language.rstrip()) 	#no whitespace at end

#To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name:
favourite_language = 'python '
favourite_language = favourite_language.rstrip()
print(favourite_language)


#strip whitespace from the left side of a string using the lstrip() method
#from both sides at once using strip():
favourite_language = ' python '
print(favourite_language.rstrip())
print(favourite_language.lstrip())
print(favourite_language.strip())

#In the real world, these stripping functions are used most often to clean up user input before it’s stored in a program.


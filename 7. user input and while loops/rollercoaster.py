''' How the input() function Works '''

print("\n''' Using int() to Accept Numerical Input '''")

age = input("How old are you? ")
print(age)      # a string

# use int() function to treat input as a numerical value

age = input("How old are you? ")
age = int(age)
print(age)      # an integer

# Python interpreted the input as a string because the number is 
# enclosed in quotes. To be an integer it need to use int() function.


print("''' Using int() to Accept Numerical Input '''")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
  print("\nYou're tall enough to ride!")
else:
  print("\nYou'll be able to ride when you're little older.")
  

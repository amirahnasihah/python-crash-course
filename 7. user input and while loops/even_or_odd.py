''' How the input() function Works '''

print("''' Using int() to Accept Numerical Input '''")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
  print("\nYou're tall enough to ride!")
else:
  print("\nYou'll be able to ride when you're little older.")


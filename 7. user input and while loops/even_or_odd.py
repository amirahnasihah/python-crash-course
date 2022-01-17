''' How the input() Function Works '''

print("''' The Modulo Operator (%) '''")

# useful tool to work with numerical info (%) which divides one number by another number and returns the remainder.

print(4 % 3)


number = input("Enter a number, and I'll tell you if it's code or odd: ")
number = int(number)

if number % 2 == 0:
  print(f"\nThe number {number} is even.")
else:
  print(f"\nThe number {number} is odd.")
  
# (how to read) if the modulo of a number and two is zero 
# (here, if number % 2 == 0) the number is even.

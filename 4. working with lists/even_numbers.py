# range() to Make a List of Numbers |convert range() into list()|
# wrap list() around a call to the range() function.
print("\nUse range() into list():")
numbers = list(range(1, 6))
print(numbers)

print("\nUse range() to skip numbers:")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(5, 13, 3))
print(odd_numbers)


# Simple Statistics with a List of Numbers
print("\n\nSimple Statistics:")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Min:")
print(min(digits))

print("Max:")
print(max(digits))

print("Sum:")
print(sum(digits))

# OR Different ways of print
print("\n\nSimple Statistics in diff print:")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Min: {min(digits)}")
print(f"Max: {max(digits)}")
print(f"Sum: {sum(digits)}")
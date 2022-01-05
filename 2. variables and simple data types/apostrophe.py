# Avoiding Syntax Errors with Strings; pg62

# syntax error, use an apostrophe within single quotes, you’ll produce an error.

# apostrophe appears inside a set of double quotes, so the Python interpreter has no trouble reading the string correctly:
message = "One of Python's strength is its diverse community."
print(message)


# single quotes, Python can’t identify where the string should end:
message = "\nOne of Python's strengths is its diverse community."
print(message)

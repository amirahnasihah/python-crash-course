filename = '10. exercises/learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)


print("\n--- Looping over the lines / reading line by line:")
with open(filename) as f:
    for line in f:
        print(line.strip())


print("\n--- Storing the lines in a list / outside the with block:")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())


print("\n--- Working with a File’s Contents:")

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    
print(pi_string)
print(len(pi_string))
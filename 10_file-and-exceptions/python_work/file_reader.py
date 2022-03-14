print("\n''' File Paths '''")

file_path = 'python_work\\text_files\\filename.txt'

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)


print("'''\nreadlines() takes each line and stores in a list:'''")

filename = 'python_work/text_files/filename.txt'

with open(filename) as file:
    lines = file.readlines()
    
for line in lines:
    print(line)
    
# the readlines() method takes each line from the file and stores it in a list. 
# this list is then assigned to lines, which we can continue to work with after the with block ends.

# Python readline() method will return a line from the file when called. readlines() method will return all the lines in a file in the format of a list where each element is a line in the file.
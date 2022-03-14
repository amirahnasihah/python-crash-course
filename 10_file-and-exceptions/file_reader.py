''' Reading from a File '''
print("''' Reading an Entire File '''")

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip()) # If want to remove the extra blank line, use rstrip() or ...
# print(contents)


print("\n''' File Paths '''")

with open('python_work/text_files/filename.txt') as file_object:
    contents = file_object.read()
print(contents)


print("\n''' Reading Line by Line '''")

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) # find more blank lines; use rstrip() to eliminate blank lines.


print("\n''' Making a List of Lines from a File '''")

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() # readlines() method takes each line from the file and stores it in a list. This list is then assigned to lines
    
for line in lines:
    print(line.rstrip())
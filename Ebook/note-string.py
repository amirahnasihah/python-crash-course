name = "nasihah"
message = "my name is"
print(f"\n{message} {name}")
print("my name is " + name + '\n')
#concatenate(plus sign) (rapatkan 2 string. diff than f-string)
#can only concatenate list (not "str") to list



motorcyles = ['honda', 'yamaha', 'suzuki']
print('seha' + 'zily')
print("kanna kamui" + " kobayashi")
print(f"{motorcyles}, this show lists and using fstring")


variable = ('nasihah')
print('\n' + variable + ' variable using plus sign')


lists = ['seha', 'zily', 'eunji']
#print(lists + ' plus sign with lists')
# lists cannot be concatenated with plus sign
# use f-string

lists = ['jeong', 'yunho', 'kobayashi']
print(f"\n{lists} this is lists using f-string")
#works fine


# lists + lists (string to list cant use plus sign)
lists = ['jeong', 'yunho', 'kobayashi']
motorcyles = ['honda', 'yamaha', 'suzuki']
print(lists + motorcyles)


# lists(index) with title() method
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("\n" + bicycles[0])
print(bicycles[1].title())


# strip string & double method title().strip()
name = " jeong eunji "		#double method used; title().strip()
print(f"\n{name.title().strip()} is:\n\tActress\n\tApink member\n\tDJ")
print(name.rstrip())
print(name.lstrip())
print(f"{name.strip()}\n")
# lists cant be double method OR title() method


# How to capitalize the title of each string in a list?
# Just iterate over the name list and then for each name, 
# change the case of first letter only by specifying the index number of first letter. 
# And then add the returned result with the 
# remaining chars then finally append the new name 
# to the already created empty list.

import re
strings = input("Please enter a list of strings: ")
List = [re.sub(r'^[A-Za-z]|(?<=\s)[A-Za-z]', lambda m: m.group().upper(), name) for name in strings.replace('"','').replace('[','').replace(']','').split(",")]
print(List)


# del statement
motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

del motorcyles[1]
del motorcyles[0]
print(motorcyles)


del(motorcyles[0])

''' Simple Example '''
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

''' Checks if the current value of car is 'bmw'.
If it is, the value is printed in uppercase. If the value of 
car is anything other than 'bmw', it’s printed in title case. '''

print("''' Checking for Equality '''")
'''
car = 'audi'
car == 'bmw'	#False

single equal sign = Set the value of car equal to 'audi'
double equal == Is the value of car equal to 'bmw'?
exclamation point and an equal sign != Represents not
'''
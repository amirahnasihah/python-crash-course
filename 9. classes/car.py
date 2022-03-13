''' Working with Classes and Instances '''

print("''' The Car Class '''")

class Car:
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		
	def get_descriptive_name(self):
			"""Return a neatly formatted descriptive name."""
			long_name = f"{self.year} {self.make} {self.model}"
			return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())




print("\n''' Setting a Default Value for an Attribute '''")

class Car:
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0	#default value
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
		
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()





print("\n''' Modifying Attribute Values '''")
print(f"3 ways: directly, through a method, incrementing through a method → ")
#3 ways: directly, through a method, incrementing through a method.


"""Modifying an Attribute's Value Directly"""


# class Car:
	# --snip-- (same as above)
	
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# use dot noation to access attribute & set its value directly thru instance.
my_new_car.odometer_reading = 23
my_new_car.read_odometer()



"""Modifying an Attribute's Value Through a Method"""


class Car:
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"\n {self.year} {self.make} {self.model}"
		return long_name.title()
			
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")
		
	def update_odometer(self, mileage):
		"""Set the odometer_reading to the given value."""
		self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()


"""Incrementing an Attribute's Value Through a Method"""


class Car:
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0	#default value
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"\n{self.make} {self.model} {self.year}"
		return long_name.title()
			
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")
		
	def update_odometer(self, mileage):
		"""
		Set the odometer_reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cant roll back an odometer!")
				
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
			
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

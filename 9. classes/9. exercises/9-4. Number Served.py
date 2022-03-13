class Restaurant():
	"""A class representing a restaurant."""
	
	def __init__(self, name, cuisine_type):
		"""Initialize a restaurant."""
		self.name = name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0 #default value
		
	def describe_restaurant(self):
		"""Display a summary of the restaurant."""
		msg = f"{self.name} serves wonderful {self.cuisine_type}."
		print(f"\n{msg}")
	
	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		msg = f"{self.name} is open. Come on in!"
		print(msg)
	
	
	def set_number_served(self, number_served):
		"""Allow user to set the number of customers that have been served."""
		self.number_served = number_served
		
	def increment_number_served(self, additional_served):
		"""Allow user to increment the number of customers served."""
		self.number_served += additional_served
	
restaurant = Restaurant('kedai mamak', 'spagetti carbonara')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 430	#modify attributes values
print(f"\nNumber served: {restaurant.number_served}")


restaurant.set_number_served(30)
print(f"\nNumber served: {restaurant.number_served}")

restaurant.increment_number_served(40)
print(f"\nNumber served: {restaurant.number_served}")
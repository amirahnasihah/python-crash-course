class Restaurant:
    """A simple attempt to represent a restaurant."""
    
    def __init__(self, nname, cuisine_type):
        """Initialize name and type attributes."""
        self.name = nname.title()
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Description of a restaurant name."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")
        
    def open_restaurant(self):
        """Simulate a restaurant is opening."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")
        
#instance called restaurant from class.
#print attributes individually
restaurant = Restaurant('shangri la', 'rattatouille')
print(restaurant.name)
print(restaurant.cuisine_type)

#calling both methods/functions
restaurant.describe_restaurant()
restaurant.open_restaurant()


#looked carefully at diff between parameter nname, attributes nname and value associated with parameter self.name 
# variable that have access through instances are called attributes (nname)
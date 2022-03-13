class Restaurant:
    """A simple attempt to represent a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize name and type attributes."""
        self.restaurant_name = name.title()
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Description of a restaurant name."""
        print(f"This restaurant named as {self.name}.")
        print(f"Its specialty is {cuisine_type}.")
        
    def open_restaurant(self):
        """Simulate a restaurant is opening."""
        print(f"Today's menu is {cuisine_type} in the house.")
        
restaurant = Restaurant('shangri la', 'rattatouille')

print(f"The best restaurant is {restaurant.restaurant_name}!")
print(restaurant.cuisine_type)
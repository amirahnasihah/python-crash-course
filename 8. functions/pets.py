''' Passing Arguments '''

print("''' 1. Positional Arguments '''")

def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster', 'harry')


print("\n''' Multiple Function Calls '''")

def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


print("\n''' Order Matters in Positional Arguments ''")

def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('harry', 'hamster')


print("\n\n''' 2. Keyword Arguments '''")

def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(animal_type='hamster', pet_name='harry')


print("\n''' Default Values '''")

def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(pet_name='willie')
describe_pet('yunho')


print("\n''' Equivalent Function Calls '''")
# have several same ways to call a function.
# all of the following calls would work for this function.

def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type} and named {pet_name.title()}.")
    
# a dog name Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# a hamster named harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
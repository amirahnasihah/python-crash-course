''' Passing a List '''

print("''' Modifying a List in a Function '''")

# The following code does this without using functions:
# ↓↓↓↓↓

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move/pass each design to completed_models after printing.
while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print(f"Printing model: {current_designs}")
    completed_models.append(current_designs)
    
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
    


print("\n\nReorganize code with two functions:↓↓\n")

# First function handle designs printing, second summarize completed prints.
# ↓↓↓↓↓

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Printing model: {current_designs}")
        completed_models.append(current_designs)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)




print("\n''' Preventing a Function from Modifying a List '''")

# want to keep original list.
# can address this issue by passing the function a copy of the list, not the original.
# function_name(list_name[:])

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Printing model: {current_designs}")
        completed_models.append(current_designs)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print_models(unprinted_designs[:], completed_models)

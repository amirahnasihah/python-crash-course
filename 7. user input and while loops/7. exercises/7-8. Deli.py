# make a list.
sandwich_orders = ['chicken', 'tuna', 'meat', 'salad']
# empty list.
finished_sandwiches = []

# want to move from sandwich_orders to finished_sandwiches.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwiches.")
    finished_sandwiches.append(current_sandwich)
    
# show finished_sandwiches info.
print("\nThe following sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(f"I made {sandwich} sandwiches.")
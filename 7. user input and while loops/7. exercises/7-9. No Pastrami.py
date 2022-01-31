sandwich_orders = [
    'chicken', 'meat', 'pastrami', 'tuna', 'salad','pastrami', 'prawn', 'pastrami'
]
finished_sandwiches = []

# out of stock 'pastrami'
print("Sorry, we are all out of stock for pastrami sandwich.\n")
# remove all 'pastrami'.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
# move item to another list.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
# item from sandwich_orders removed, assigned to current_sandwich, then added to finished_sandwiches.
    finished_sandwiches.append(current_sandwich)

# showing all items beautifully.
for sandwich in finished_sandwiches:
    print(f"We have {sandwich} sandwiches only.")
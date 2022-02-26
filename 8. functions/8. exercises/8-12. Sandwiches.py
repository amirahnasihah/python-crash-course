def order_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nList of items a person wants on a sandwich:")
    print("I'll make you a great sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

# the way I answered ↓↓↓↓        
#items = ['cheese', 'salad', 'ham', 'tomato', 'ketchup']
#sandwich_order(items)

# Matt answer:
order_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
order_sandwich('turkey', 'apple slices', 'honey mustard')
order_sandwich('peanut butter', 'strawberry jam')
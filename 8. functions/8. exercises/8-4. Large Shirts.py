# default value = 'large'
def make_shirt(size='large', message='I love Python!'):
    """Tshirt summary"""
    print(f"\nThis shirt's size is {size}.")
    print(f"The printed text on shirt written as {message}")
    
# keyword arguments.
make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='Go Python!')
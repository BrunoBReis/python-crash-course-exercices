def make_pizza(*toppings:str):
    """Print the list of toppings"""
    for topp in toppings:
        print(topp)

make_pizza('mushrooms', 'green peppers', 'extra cheese')
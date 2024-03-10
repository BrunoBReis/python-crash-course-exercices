def sandwiche(*items: str):
    """Make a sandwiche"""
    print('Here is your sandwich\n')
    for item in items:
        print(f"\t{item}")

sandwiche('Turkey', 'Swiss Cheese', 'Cranberry Sauce', 'Lettuce')
sandwiche('Chicken', 'Avocado', 'Bacon', 'Tomato')
sandwiche('Salami', 'Provolone Cheese', 'Roasted Red Peppers', 'Spinach')

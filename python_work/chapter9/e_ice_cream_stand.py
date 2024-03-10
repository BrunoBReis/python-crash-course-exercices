from e_restaurant2 import Restaurant

class IceCreamStand(Restaurant):
    """Creating an Ice Cream restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        """Inicialize IceCream class"""
        super().__init__(restaurant_name, cuisine_type)
        # Default Values
        self.flavors = flavors

    def show_flavors(self):
        """Prints all flavors"""
        for flavor in self.flavors:
            print(flavor)

restaurant = IceCreamStand('Best Flavor', 'Ice Cream', ['Vanilla', 'Chocolate', 'Strawberry'])
restaurant.show_flavors()    
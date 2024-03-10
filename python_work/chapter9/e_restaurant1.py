class Restaurant:
    """Creating a resturant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe restaurant"""
        print(f'The {self.restaurant_name} has {self.cuisine_type}')

    def open_resturant(self):
        """Prints restaurant is open"""
        print(f"The {self.restaurant_name} is open!")

my_restaurant = Restaurant('FusionFlavors', 'Global Fusion')

my_restaurant.describe_restaurant()
my_restaurant.open_resturant()
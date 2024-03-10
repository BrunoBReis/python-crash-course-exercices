class Restaurant:
    """Creating a resturant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Default value
        self.number_served = 0

    def describe_restaurant(self):
        """Describe restaurant"""
        print(f'The {self.restaurant_name} has {self.cuisine_type}')

    def open_resturant(self):
        """Prints restaurant is open"""
        print(f"The {self.restaurant_name} is open!")
    
    def set_number_served(self, amount):
        """Set number served"""
        self.number_served = amount
    
    def increment_number_serverd(self, amount):
        """Increment number served"""
        if amount >= 0:
            self.number_served += amount
        else:
            print(f"Can't increment {self.number_served} to {amount}")

restaurant = Restaurant('FusionFlavors', 'Global Fusion')

print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(20)
print(restaurant.number_served)
restaurant.increment_number_serverd(5)
print(restaurant.number_served)

from random import randint


class Die:
    """Class represents sigle die"""

    def __init__(self, num_sides=6):
        """Initializes die"""    
        self.num_sides = num_sides
    
    def roll(self):
        """Return a value of dice"""
        return randint(1, self.num_sides)

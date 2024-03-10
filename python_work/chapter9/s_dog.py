class Dog:
    """Creating a dog"""

    def __init__(self, name, age):
        """Initialize attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Dog sits"""
        print(f'{self.name} is now sitting.')
    
    def roll_over(self):
        """Dog rolls over"""
        print(f'{self.name} rolled over.')

my_dog = Dog('Wille', 6)

print(f"My dog name is {my_dog.name}")
print(f"My dog age is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()
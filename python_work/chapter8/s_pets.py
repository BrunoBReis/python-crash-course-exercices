# Positional arguments

def describe_pet(animal_type, pet_name, years=2):
    """Display information about pet"""
    print(f'My pet is a {animal_type.title()}')
    print(f"It name is {pet_name.title()}")
    print(f'It is {years}')

describe_pet('dog', 'cuttie')
describe_pet(pet_name='cuitte', animal_type='dog')
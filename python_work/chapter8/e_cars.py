def make_car(manufacturer: str, model_name: str, **attributes: dict):
    """Describes a car"""
    attributes['manufacturer'] = manufacturer
    attributes['model_name'] = model_name
    return attributes

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
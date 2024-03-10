class Car:
    """Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize car"""
        self.make = make
        self.model = model
        self.year = year
        # Default value
        self.odometer = 0

    def get_descriptive_name(self):
        """Prints all information"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def read_odometer(self):
        """Reads odometer"""
        print(f"Odometer has {self.odometer} miles")

    def update_odometer(self, mileage):
        """Updates odometer value"""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print(
                f"You can't decresse odometer value {self.odometer} to {mileage}")

    def increment_odometer(self, value):
        """Increse odometer value"""
        if value >= 0:
            self.odometer += value
        else:
            print("Needs to be greater then 0")


class Battery:
    """Creates a battery"""

    def __init__(self, battery_size=40):
        """Initialize battery"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Shows battery storage"""
        print(f"This car has {self.battery_size} KWh")

    def get_range(self):
        """Shows battery range"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can drive {range} miles")


class EletricCar(Car):
    """Represent apsects of an eletric car"""

    def __init__(self, make, model, year):
        """Initilize eletric car"""
        super().__init__(make, model, year)
        # Default Values
        self.battery = Battery()


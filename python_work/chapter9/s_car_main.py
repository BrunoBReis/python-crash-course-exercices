from s_car import Car, EletricCar, Battery

# Main

# Creating a car
# car = Car('audi', 'a4', 2024)
# print(car.get_descriptive_name())

# Showing odometer
# car.read_odometer()
# car.odometer = 23
# car.read_odometer()
# car.update_odometer(0)
# car.read_odometer()
# car.increment_odometer(10)
# car.increment_odometer(-1)
# car.read_odometer()

car = EletricCar('nissan', 'leaf', 2024)
print(car.get_descriptive_name())
car.battery.describe_battery()
car.battery.get_range()

eletric_car = EletricCar('nissan', 'leaf', 2022)
eletric_car.battery = Battery(battery_size=65)

eletric_car.battery.describe_battery()
eletric_car.battery.get_range()

# Organaizng a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(f"Original list\n{cars}")
print(f"Changed list\n{sorted(cars)}")  
print(f"Original list\n{cars}")

# Note: it's important to use lowercase to sort. In uppercase could lead an error

# Reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Original list\n{cars}")
cars.reverse()
print(f"Reversed list\n{cars}")
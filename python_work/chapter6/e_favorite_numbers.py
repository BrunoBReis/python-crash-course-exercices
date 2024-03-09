# Working with dictionary

people = {
    "Alice": [13, 17, 22],
    "Bob": [20, 2, 0],
    "Charlie": [7, 14, 21],
    "Diana": 10,
    "Ethan": 42,
}

for name, numbers in people.items():
    print(name)
    try:
        for number in numbers:
            print(number)
    # It's the error for not be in list
    except (TypeError):
        print(numbers)

print("-------")

# Better code
for name, numbers in people.items():
    print(name)
    # Verifies if numbers is a list
    if isinstance(numbers, list):
        for number in numbers:
            print(f"\t{number}")
    else:
        print(f"\t{numbers}")
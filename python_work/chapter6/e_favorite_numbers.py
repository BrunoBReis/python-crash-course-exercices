# Working with dictionary

people = {
    "Alice": [13,17,22],
    "Bob": [20, 2, 0],
    "Charlie": [7, 14, 21],
    "Diana": 10,
    "Ethan": 42,
}

for key, value in people.items():
    print(f"{key} likes number {value}")
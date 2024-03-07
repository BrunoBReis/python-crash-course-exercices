# Slicing the list

pizzas = ["Pepperoni", "Margherita", "Hawaiian", "Vegetarian", "Meat Lover's"]

for pizza in pizzas[:3]:
    print(f'I love {pizza}')

for pizza in pizzas[2:4]:
    print(f"I love even more {pizza}")

for pizza in pizzas[3:]:
    print(f"I love more more more {pizza}")
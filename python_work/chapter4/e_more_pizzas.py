# Adding more pizzas

pizzas = ["Pepperoni", "Margherita", "Hawaiian", "Vegetarian", "Meat Lover's"]

friend_pizzas = pizzas[:]

# Adding new pizzas
pizzas.append("Buffalo Chicken")
friend_pizzas.append("Brocolis Pizza")

print("My favorite pizzas:\n")
for pizza in pizzas:
    print(pizza)

print("-------")

print("My friend favorite pizzas:\n")
for pizza in friend_pizzas:
    print(pizza)
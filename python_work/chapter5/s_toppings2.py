# Toppings

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# Checking if list is not empty
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we are out of {requested_topping}.")
else:
    print("List is empty")

print("\nFinished making your pizza!")

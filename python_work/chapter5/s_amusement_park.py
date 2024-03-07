# Cost for each age

your_age = 12

if your_age < 4:
    print("Your adimition cost is 0 dollars")
elif your_age < 18:
    print("Your adimition cost is 25 dollars")
else:
    print("Your adimition cost is 40 dollars")
    
# Simplifing this code

your_age = 2

if your_age < 4:
    price = 0
elif your_age < 18:
    price = 25
else:
    price = 40
    
print(f"Your adimition cost is {price} dollars")

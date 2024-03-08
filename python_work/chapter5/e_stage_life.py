import random
# Stages of life

age = random.randint(1, 101)

if age < 2:
    state = 'a baby'
elif age >= 2 and age < 4:
    state = 'a toddler'
elif age >= 4 and age < 13:
    state = 'a kid'
elif age >= 13 and age < 20:
    state = 'a teenager'
elif age >= 20 and age < 65:
    state = 'an adult'
else:
    state = 'an elder'

print(f"You're {state}")

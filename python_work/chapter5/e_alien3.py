import random
# Simple alien game
alien_colors = ['green', 'yellow', 'red']

# Randomize an color from alien_colors
alien_color = alien_colors[random.randint(0,len(alien_colors))]
    
# Separete points for each alien_color
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15

print(f"I've got {point} points")

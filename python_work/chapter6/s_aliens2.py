# Nesting alines

# Creating aliens
alien_green = {
    'color' : 'green',
    'points' : 5,
}

alien_yellow = {
    'color' : 'yellow',
    'points' : 10,
}

alien_red = {
    'color' : 'red',
    'points' : 20,
}

battle_field = []

for alien_count in range(10):
    battle_field.append(alien_green)
for alien_count in range(20):
    battle_field.append(alien_yellow)
for alien_count in range(10):
    battle_field.append(alien_red)

print(len(battle_field))

points = 0
# How many points do I have
for alien in battle_field:
    # For each alien search for value
    for key, value in alien.items():
        if key == 'points':
            points += value

print(points)

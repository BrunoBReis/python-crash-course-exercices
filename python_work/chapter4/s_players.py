# Slicing a list 

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[:4])
print(players[1:4])
print(players[2:])
print(players[-2:])

# An example with loop
for name in players[3:]:
    print(f'I like {name.title()}')
# Slicing a list with [start:end]
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Slicing from the beginning to the fifth element
print(players[:4])

# Slicing from third index to end
print(players[2:])

# Get the last three players in the list
print(players[-3:])

# Loop through the first three players in the list
for player in players[:3]:
    print(player.title())




cars = ['bmw', 'porsche', 'volkswagen', 'audi', 'volvo', 'mercedes']

# sort will modify the list
cars.sort()
print(f'The list sorted by sort(): {cars}')

cars.sort(reverse=True)
print(f'The list sorted in reverse: {cars}')

cars = ['bmw', 'porsche', 'volkswagen', 'audi', 'volvo', 'mercedes']
print('List of cars has been reverted to original declaration')

# sorted will return a sorted list instead of modifying the original
print(f'List sorted by sorted(): {sorted(cars)}')

# the reverse function will reverse the contents of a list, permanently
cars.reverse()
print(f'List reversed by reverse(): {cars}')

# the len function will provide the length of a list
print(f'Length of the list as calculated by len(cars): {len(cars)}')
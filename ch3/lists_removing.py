motorcycles = ['honda', 'yamaha', 'suzuki']

# del will remove an item at the specified index
del motorcycles[1]
print(motorcycles)

# pop will remove the last item of the list and return it
popped = motorcycles.pop()
print(popped)

motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('triumph')

# pop can be used with an index to remove a value
motorcycles.pop(0)
print(motorcycles)

# remove will will delete the specified value from a list
motorcycles.remove('suzuki')
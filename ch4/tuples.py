dimensions = (200, 50)
print(dimensions)

# Tuples' values cannot be reassigned

# A tuple with only one element needs a comma
my_t = (2,)

# Looping a tuple works the same way as a list
for dimension in dimensions:
    print(dimension)

# You can, however, reassign a new tuple to an existing tuple
new_dimenions = (300, 75)
dimensions = new_dimenions
print(dimensions)
# creating a list from 1 to 4
for value in range(1, 5):
    print(value)

# creating a list from 1 to 5
numbers = list(range(1,6))
print(numbers)

# range() creates a list of numbers and stops appending
# at the value of the second parameter. That is to say
# that the last value is not added to the list.

# the third parameter for range() is a step size
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# creating a list of the first 10 square numbers
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
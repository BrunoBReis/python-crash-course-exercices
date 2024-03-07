import math
# Creating a list of square numbers

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# Using list Comprehension

cubics = [value ** 3 for value in range(1,11)]
print(cubics)

# Testing Comprehension

# Creating an equation function 
def equation_function(number):
    """ Calucating area of circle """
    return f"{(number ** 2 * math.pi):.2f}"

# Using the function into a list
areas = [equation_function(number) for number in range(1,10)]

print(areas)
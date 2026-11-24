# Question:
# Find the product of squares of numbers greater than 5.

from functools import reduce

numbers = [2, 6, 3, 8, 4, 10]

greater = filter(lambda n: n > 5, numbers)# Step 1: Filter numbers greater than 5


square = map(lambda s: s ** 2, greater)# Step 2: Calculate their squares


product = reduce(lambda a,b: a * b,square)# Step 3: Calculate their product


print(product)# Print the result
# logic in this program we need find the greater no so use filter and cal square we need map function also 
#also to product entire list we need to use the reduce for it 
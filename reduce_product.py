# The reduce() function is used to perform an operation repeatedly on elements of a collection and produce a single final result.
from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print(product)
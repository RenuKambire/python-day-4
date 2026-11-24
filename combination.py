# Question:
# Find the sum of cubes of only the even numbers.

from functools import reduce

numbers = [2, 3, 4, 5, 6]

even_no = filter(lambda n:n % 2 == 0, numbers)# Step 1: Filter even numbers


cubes_no = map(lambda n: n ** 3,even_no)# Step 2: Calculate their cubes


sum_no = reduce(lambda a,b :a + b,cubes_no) # Step 3: Calculate their sum

print(sum_no)
# Print the final result
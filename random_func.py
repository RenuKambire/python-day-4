
# Question 6:
# Create a program that generates a random number
# between 1 and 100.
#
# Check whether the generated number is even or odd.
# Display both the generated number and its result.

import random

num = random.randint(1, 100)

print("Generated number:", num)

if num % 2 == 0:
    print("Result: Even number")
else:
    print("Result: Odd number")

# Question:
# Find the total marks of students who scored
# more than 60 after increasing their marks by 5.

from functools import reduce

marks = [45, 65, 80, 55, 70]

# Step 1:
increase_marks = map(lambda m : m + 5, marks)


# Step 2:
students = filter(lambda s : s > 60,increase_marks)

# Step 3:
total = reduce(lambda a, b : a + b,students)

# Print result
print(total)
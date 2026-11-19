numbers = [12, 45, 23, 45, 67, 12, 89, 67]

largest = 0
second_largest = 0

for i in numbers:
  if i > largest:
    second_largest = largest
    largest = i
  elif i<largest and i>second_largest:
    second_largest = i
print(second_largest)
  

 

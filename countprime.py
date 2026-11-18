
# Function 1: Check whether a number is prime

def is_prime(num):
  if num <= 1:
    return False
    
  for i in range(2,num):
    if num % i == 0:
      return False
  return True       

# Function 2: Count prime numbers till N

def count_primes(N):
  count = 0
  for i in range(2,N+1):
    if is_prime(i):
      count += 1
  return count
  
# Main program

N = 20
result = count_primes(N)
print("count", result)



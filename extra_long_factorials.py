from math import factorial

n = 30
# M1: Using the math module
print(factorial(n))

# M2: Manually looping through the numbers
o = 1
print([o := o * i for i in range(1, n + 1)].pop())

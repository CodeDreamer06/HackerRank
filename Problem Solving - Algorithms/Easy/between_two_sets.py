from math import lcm, gcd

a = [2, 6]
b = [24, 36]

g, l = gcd(*b), lcm(*a)
print(sum([g % i == 0 for i in range(l, g + 1, l)]))
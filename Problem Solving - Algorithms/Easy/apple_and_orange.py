s, t = 7, 11
a, b = 5, 15
m, n = 3, 2
md, nd = [-2, 2, 1], [5, -6]
mh, nh = 0, 0

print(sum(s <= a + d <= t for d in md))
print(sum(s <= b + d <= t for d in nd))
x1, v1 = 43, 2
x2, v2 = 70, 2

jumps = (x2 - x1)/(v1 - v2) if v1 != v2 else -1
print('YES' if 0 <= jumps == int(jumps) else 'NO')
x, y, z = 1, 3, 2
a, b = abs(x - z), abs(y - z)

print('Cat A' if a < b else 'Cat B' if a > b else 'Mouse C')

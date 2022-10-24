a = [17, 28, 30]
b = [99, 16, 8]

results = [0] * 3

for i in range(3):
    results[0 if a[i] > b[i] else 1 if a[i] < b[i] else 2] += 1

print(results[:-1])


b = 60
keyboards, drives = [40, 50, 60], [5, 8, 12]

totals = []

for keyboard in keyboards:
    for drive in drives:
        totals.append(keyboard + drive)

print(max(t for t in totals if t <= b))

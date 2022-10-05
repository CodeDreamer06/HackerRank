steps = 'UDDDUDUU'
current_altitude, valley_count = 0, 0

for step in steps:
    current_altitude += 1 if step == 'U' else -1
    valley_count += 1 if current_altitude == -1 and step == 'D' else 0

print(valley_count)

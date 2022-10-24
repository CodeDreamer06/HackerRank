from collections import defaultdict
import statistics

birds = [1, 4, 4, 4, 3, 3, 5, 3]

# M1: Using the statistics module
print(min(statistics.multimode(birds)))

# M2: Manually looping through the list
common = defaultdict(int)
highest_key, highest_count = 0, 0

for bird in birds:
    common[bird] += 1

for key, value in common.items():
    if value > highest_count:
        highest_count = value
        highest_key = key

    elif value == highest_count:
        if key < highest_key:
            highest_key = key

print(highest_key)

scores = [12, 24, 10, 24]
lowest = highest = scores[0]
records = [0] * 2

for score in scores:
    if score > highest:
        highest = score
        records[0] += 1
    if score < lowest:
        lowest = score
        records[1] += 1

print(records)
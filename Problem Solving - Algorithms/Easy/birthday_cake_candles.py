candles = [4, 4, 1, 3]

# M1: Using built-in functions
print(candles.count(max(candles)))

# M2: Manually looping through the list
max, count = 0, 0
for candle in candles:
    if candle > max:
        max = candle
        count = 1
    elif candle == max:
        count += 1

print(count)

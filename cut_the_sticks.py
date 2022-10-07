sticks = [5, 4, 4, 2, 2, 8]
sticks.sort()
count = 0

print([len(sticks)] + [remaining := len(sticks) - (count := count + sticks.count(i)) for i in sorted(set(sticks))][:-1])

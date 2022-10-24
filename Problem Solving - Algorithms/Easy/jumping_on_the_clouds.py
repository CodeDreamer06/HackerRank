c = [0, 1, 0, 0, 0, 1, 0]

jumps = 0

for i in range(len(c)):
    if c[i] == 1:
        jumps += 1

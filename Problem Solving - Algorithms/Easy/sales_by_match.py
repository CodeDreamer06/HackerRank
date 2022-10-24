socks = [1, 2, 1, 2, 1, 3, 2]
n = 7

current_pairs, pairs = set(), 0

for sock in socks:
    if sock in current_pairs:
        pairs += 1
        current_pairs.remove(sock)

    else:
        current_pairs.add(sock)

print(pairs)

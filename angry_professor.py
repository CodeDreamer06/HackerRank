k = 2
arrivals = [0, -1, 2, 1]

print('YES' if sum(i <= 0 for i in arrivals) < k else 'NO')

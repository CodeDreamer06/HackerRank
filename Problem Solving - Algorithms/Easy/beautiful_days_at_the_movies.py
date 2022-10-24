i, j, k = 20, 23, 6
print(sum(abs(int(str(n)[::-1]) - n) % k == 0 for n in range(i, j + 1)))

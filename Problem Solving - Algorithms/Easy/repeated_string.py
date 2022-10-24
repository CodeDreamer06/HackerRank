s, n = 'abcaca', 10

print(s.count('a') * (n // len(s)) + s[:n % len(s)].count('a'))

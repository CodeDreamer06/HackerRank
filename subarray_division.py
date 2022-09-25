from queue import Queue

s = [2, 2, 1, 3, 2]
m, d = 2, 4

# M1: Use a queue
q = Queue(maxsize = m)
total_sum, possibilities = 0, 0

for i in s:
    total_sum += i if not q.full() else i - q.get()
    q.put(i)

    if total_sum == d:
        possibilities += 1

print(possibilities)

# M2: Use a list
sector = []
total_sum, possibilities = 0, 0

for i in s:
    total_sum += i if len(sector) < m else i - sector.pop(0)
    sector.append(i)
    
    if total_sum == d:
        possibilities += 1
    
print(possibilities)

# M3: Use list comprehension
print(sum([sum(s[i:i + m]) == d for i in range(len(s))]))
n = 10

print(sum((x := int(i)) != 0 and n % x == 0 for i in str(n)))

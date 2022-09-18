array = [1, 1, 0, -1, -1]
print(f'{sum(1 for i in array if i > 0)/len(array):.6f}')
print(f'{sum(1 for i in array if i < 0)/len(array):.6f}')
print(f'{sum(1 for i in array if i == 0)/len(array):.6f}')
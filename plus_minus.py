array = [1, 1, 0, -1, -1]
print(f'{sum(i > 0 for i in array)/len(array):.6f}')
print(f'{sum(i < 0 for i in array)/len(array):.6f}')
print(f'{sum(i == 0 for i in array)/len(array):.6f}')
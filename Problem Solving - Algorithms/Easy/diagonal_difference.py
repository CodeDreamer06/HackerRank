array = [[1, 2, 3],
         [4, 5, 6],
         [9, 8, 9]]
         
side = len(array[0])
print(abs(sum([array[i][i] - array[i][side - i - 1] for i in range(side)])))
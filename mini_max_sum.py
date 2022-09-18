array = [3, 5, 1, 7, 9]
# M1: Using a sorted array
sorted_array = sorted(array)
print(f'{sum(sorted_array[:-1])} {sum(sorted_array[1:])}')

# M2: Without sorted array
result, minimum, maximum = 0, float('inf'), 0
for i in range(len(array)):
    result += array[i]
    if array[i] < minimum:
        minimum = array[i]
    if array[i] > maximum:
        maximum = array[i]

print(f'{result - maximum} {result - minimum}')

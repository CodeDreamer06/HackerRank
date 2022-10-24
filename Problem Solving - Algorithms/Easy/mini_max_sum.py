array = [3, 5, 1, 7, 9]
# M1: Using a sorted array
sorted_array = sorted(array)
print(f'{sum(sorted_array[:-1])} {sum(sorted_array[1:])}')

# M2: Without sorted array
result, minimum, maximum = 0, float('inf'), 0
for i in array:
    result += i
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i

print(f'{result - maximum} {result - minimum}')

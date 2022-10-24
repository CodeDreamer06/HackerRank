from statistics import mode

numbers = [1, 2, 2, 3]

print(len(numbers) - numbers.count(mode(numbers)))

width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]

print([min(width[case[0]:case[1] + 1]) for case in cases])

bill = [3, 10, 2, 9]
k, b = 1, 7

fair_split = (sum(bill) - bill[k]) // 2
print('Bon Appetit' if fair_split == b else b - fair_split)
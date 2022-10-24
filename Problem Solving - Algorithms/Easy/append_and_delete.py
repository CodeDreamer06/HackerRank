# s, t = 'ashley', 'ash'
s, t = 'hackerhappy', 'hackerrank'
k = 9

# Remove the common elements
# Add the count of the remaining letters in s from the total length
# Add the count of the remaining letters in t from the total length

minimum_len = min(len(s), len(t))
comparison = [s[i] == t[i] for i in range(minimum_len)]
remaining_count = len(s) - comparison.index(False) if not all(comparison) else minimum_len

print(remaining_count)


# comparison = [s[i] == t[i] for i in range(min(len(s), len(t)) - 1)]
# print(len(s) - (x := 0 if all(comparison) else comparison.index(False)))
# print(len(t) - x)
# print('Yes' if k >= len(s) - (x := 0 if all(comparison) else comparison.index(False)) + len(t) - x else 'No')

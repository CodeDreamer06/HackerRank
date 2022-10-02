ar = [1, 2, 3, 4, 5, 6]
k, n = 5, len(ar)

# Temp method:
# print(sum([(ar[i] + ar[j]) % k == 0 and i != j for i in range(n)
#   for j in range(i, n)]))

# We need to find the number of possible ways where the sum of two integers is divisible by k.
# Divide all the numbers of the list and save their mods.
# [1, 2, 3, 4, 0, 1]
# Now, we just need to find another

visited = set()
possibilities = 0
for i in ar:
    if i in visited:
        possibilities += 1
        print('Found:', i)

    r = i % k
    visited.add(5 - r if r != 5 else 0)

    print(i, visited)

print(visited, possibilities)


# for i in range(len(ar)):
#     for j in range(i, len(ar)):
#         print((i + j) % 5 == 0)

# numbers = []
# possibilities = 0

# for i in ar:
#     if i not in numbers:
#         numbers.append(i)

#     # Find the number of numbers where (i + j) % 5 == 0
#     # Let's say the number we just got is 4.
#     # Now we need to find if there is another number in the set, who can be added to be divisible by 5.

#     for n in numbers:
#         if (i + n) % 5 == 0:
#             print(i, n)
#             possibilities += 1
#             numbers.remove(i)

#     # if sum_goal - i in numbers:
#     #     possibilities += 1

# print(possibilities)

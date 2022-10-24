from string import ascii_lowercase

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5]
word = 'torn'

print(len(word) * max([h[ascii_lowercase.index(letter)] for letter in word]))

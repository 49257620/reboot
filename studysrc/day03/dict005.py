# encoding: utf-8
# author = ‘LW’

my_dict = {'I': 5, 'w': 8, 'a': 18, 's': 20, 'n': 17, 'o': 24, 't': 23, 'd': 13, 'e': 39, 'l': 12, 'i': 20, 'v': 2,
           'r': 13, 'u': 8, 'h': 17, 'f': 6, 'c': 3, 'm': 7, 'y': 5, 'p': 8, 'g': 3, 'b': 2, 'k': 2, 'L': 1, 'j': 1,
           'T': 1}

items = list(my_dict.items())
nnn = len(items)

for i in range(nnn - 1):
    for j in range(nnn - 1 - i):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

print(items)
"""

for j in range(nnn - 1):
    for idx in range(nnn - 1 - j):
        if items[idx][1] > items[idx + 1][1]:
            items[idx], items[idx + 1] = items[idx + 1], items[idx]
"""
print(items[:-6:-1])

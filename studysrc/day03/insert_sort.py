# encoding: utf-8
# author = ‘LW’

a = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

for i in range(1, len(a)):
    idx = i
    while idx > 0 and a[idx] < a[idx - 1]:
        a[idx], a[idx - 1] = a[idx - 1], a[idx]
        print('step:', i, 'idx:', idx, a)
        idx -= 1

print('final:', a)

# encoding: utf-8
# author = ‘LW’

ll = [-1, -2, -3, -5, -10]


max_val = None

for i in ll:
    if max_val is None:
        max_val = i
    elif max_val < i:
        max_val = i

print(max_val)

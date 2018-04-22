# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


l1 = [{'name': 'll', 'age': 30}, {'name': 'll', 'age': 21}, {'name': 'll', 'age': 19}]

l2 = sorted(l1, key=lambda x: x['age'])

print(l2)
print(l1)

l1.sort(key=lambda x: x['age'])
print(l1)

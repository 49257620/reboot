# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

l1 = list(range(1, 11))

# 列表推导式
print([x ** 2 for x in l1 if x % 2 == 0])

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 字典推倒式
print({k: v * 2 for k, v in my_dict.items() if v % 2 == 0 and k != 'd'})

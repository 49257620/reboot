# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

import mysort

li_1 = [5, 4, 3, 2, 1]
mysort.fun_bubble(li_1)

print(li_1)

li_2 = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
mysort.fun_bubble(li_2, lambda x: x[1])

print(li_2)

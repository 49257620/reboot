# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’



def fun_bubble(li, key):
    length = len(li)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if key(li[j]) > key(li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]


def fun_bubble2(li, cmp):
    length = len(li)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if cmp(li[j], li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]


li_1 = [5, 4, 3, 2, 1]

# fun_bubble(li_1, lambda x: x)
fun_bubble2(li_1, lambda x, y: x > y)
print(li_1)

li_2 = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]

# fun_bubble(li_2, lambda x: x[1])
fun_bubble2(li_2, lambda x, y: x[1] > y[1])
print(li_2)

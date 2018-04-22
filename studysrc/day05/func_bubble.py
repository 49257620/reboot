# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


def key1(n):
    return n


def key2(n):
    return n[1]


def cmp1(n1, n2):
    return n1 > n2


def cmp2(n1, n2):
    return n1[1] > n2[1]


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

fun_bubble(li_1, key1)
# fun_bubble2(li_1, cmp1)
print(li_1)

li_2 = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]

fun_bubble(li_2, key2)
# fun_bubble2(li_2, cmp2)
print(li_2)

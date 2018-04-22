# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


def return_tuple():
    a = 10
    print('return a:', a)
    return (1, 2, 3, 4), 12345
    a = 20
    print('return a:', a)
    print('已经return了，看看还执行不执行')


s = return_tuple()

print(s)

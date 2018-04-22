# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
"""
LGB (local, global, build-in)
"""
g_a = 1
g_b = [1]
g_c = [1]


def test_lgb_1():
    g_a = 2  # local
    g_b = [1, 2]  # local
    g_c.append(3)  # global

    print('inner function:', g_a, g_b, g_c)


def test_lgb_2():
    global g_a, g_b  # 使用global关键字 ， 使用全局变量
    g_a = 2  # global
    g_b = [1, 2]  # global
    g_c.append(3)  # global

    print('inner function:', g_a, g_b, g_c)


test_lgb_2()
print('outer function:', g_a, g_b, g_c)

# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
"""
基本类型
应用类型

"""
g_a = 1
g_b = [1]
g_c = [1]


def test_1(a, b, c):
    a = 2  # 简单类型，新的local变量
    b = [1, 2]  # 重新赋值，改变了b的引用地址,b引用了新的local变量
    c.append(3)  # 未改变引用地址
    print('inner:', a, b, c)


test_1(g_a, g_b, g_c)
print('outer:', g_a, g_b, g_c)

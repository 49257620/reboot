# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
"""
可变参数  *args **kwargs
位置，默认值，可变列表，可变关键字
有默认值的参数后面必须都包含默认值
"""


def test_args(*args):
    print(args)


test_args(1, 2, 3, 4, 5)


def test_kwargs(**kwargs):
    print(kwargs)


test_kwargs(a='a', b=2, c=3)


# 必须使用keyword进行参数传递方式
def test_kw_must(*args, a, b, c):
    print(args, a, b, c)


# test_kw_must(1,2,3) 该种方式报错
test_kw_must(a=1, b=2, c=3)

# encoding: utf-8
"""
【程序26】
题目：利用递归方法求5!。
1.程序分析：递归公式：fn=fn_1*4!
2.程序源代码：
"""


def fn1(num):
    return 1 if num == 1 else num * fn1(num - 1)


print(fn1(5))

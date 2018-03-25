# encoding: utf-8
# author = ‘LW’
"""
元祖 ：不可变列表
不可变指的是引用和值不可变
"""

a = (1, 2, [], 3)
print('改变之前id：', id(a[2]))
a[2].append(4)
a[2].append(5)
print('改变之后id：', id(a[2]))
print('改变之后内容：', a)

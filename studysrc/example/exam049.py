# encoding: utf-8
"""
【程序49】
题目：演示lambda的使用。
1.程序分析：
2.程序源代码：

"""

MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

a = 10
b = 20
print('The largar one is %d' % MAXIMUM(a, b))
print('The lower one is %d' % MINIMUM(a, b))

list1 = [3, 5, -4, -1, 0, -2, -6]
print(sorted(list1, key=lambda x: abs(x)))


def get_y(a, b):
    return lambda x: a*x + b


y1 = get_y(1, 1)
print(y1(4))

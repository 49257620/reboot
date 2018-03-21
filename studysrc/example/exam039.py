# encoding: utf-8
"""
【程序39】
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
1. 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后
　　　　　此元素之后的数，依次后移一个位置。
2.程序源代码：
"""

num = 5

a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 1000]

idx = 0

for n, m in enumerate(a):
    if n == 0 and num <= m:
        idx = n
    elif n == a.__len__() - 1 and num >= m:
        idx = n + 1
    else:
        if m <= num <= a[n + 1]:
            idx = n + 1

print(idx)
if idx > a.__len__():
    a.append(num)
else:
    a.insert(idx, num)

print(a)

# encoding: utf-8
"""
【程序40】
题目：将一个数组逆序输出。
1.程序分析：用第一个与最后一个交换。
2.程序源代码：
"""

a = [9, 6, 5, 4, 1]

for i in reversed(a):
    print(i, end=" ")

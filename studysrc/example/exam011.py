# encoding: utf-8
"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
1.程序分析：　兔子的规律为数列1,1,2,3,5,8,13,21....
2.程序源代码：
"""


def cnt(m):
    if m < 3:
        return 1
    else:
        return cnt(m - 1) + cnt(m - 2)


for i in range(1, 10):
    print(cnt(i) * 2)
# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

"""
一共三步

把 n-1 号盘子移动到缓冲区
把1号从起点移到终点
然后把缓冲区的n-1号盘子也移到终点
"""

cnt = 0


def move(n, start, temp, end):
    if n == 1:
        global cnt
        cnt += 1
        print('Move from', start, 'to', end)
    else:
        move(n - 1, start, end, temp)
        move(1, start, temp, end)
        move(n - 1, temp, start, end)


cnt = 0
move(3, 'A', 'B', 'C')
print(cnt)

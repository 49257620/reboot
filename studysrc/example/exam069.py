# encoding: utf-8
"""
【程序69】
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出
　　　圈子，问最后留下的是原来第几号的那位。
1. 程序分析：
2.程序源代码：
"""


l = []
for i in range(1, 51):
    l.append(i)

# print(l)


def remove3(l):
    if len(l) >= 3:
        # print('a', len(l))
        i0 = l[0]
        i1 = l[1]
        l.remove(l[2])
        l.remove(l[1])
        l.remove(l[0])
        l.append(i0)
        l.append(i1)
        # print(l)
        return remove3(l)
    elif len(l) == 2:
        l.remove(l[0])
        return l


print(remove3(l)[0])

# encoding: utf-8
"""
【程序61】
题目：打印出杨辉三角形（要求打印出10行如下图）　　　
1.程序分析：
较为便捷，代码量较少的实现方式如下：
# -*- coding: utf-8 -*-
#!/usr/bin/env python
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
下面是另一种方式：
def triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
另一个不用生成器的版本：
def YangHui (num = 10):
    LL = [[1]]
    for i in range(1,num):
        LL.append([(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
    return LL
"""

LL = [[1]]
for i in range(1, 11):
    LL.append([])
    for j in range(i + 1):
        if j == 0:
            LL[i].append(LL[i - 1][j])
        elif j == i:
            LL[i].append(LL[i - 1][j - 1])
        else:
            LL[i].append(LL[i - 1][j - 1] + LL[i - 1][j])

for x in LL:
    print(x)
"""
print(1)
print(1,1)
print(1,2,1)
print(1,3,3,1)
print(1,4,6,4,1)
print(1,5,10,10,5,1)
"""

L = [1]
L.append(0)

print(L)
print(L[1 - 1])
print(L[1])

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

fun = triangles()

print(next(fun))
print(next(fun))
print(next(fun))
print(next(fun))

# encoding: utf-8
"""
【程序19】
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
　　　找出1000以内的所有完数。
1. 程序分析：请参照程序<--上页程序14.
2.程序源代码：
from sys import stdout
for j in range(2,1001):
    k = []
    n = -1
    s = j
    for i in range(1,j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)

    if s == 0:
        print j
        for i in range(n):
            stdout.write(k[i])
            stdout.write(' ')
        print k[n]


for num in range(2, 1001):
    numOld = num;
    tmp = 0
    for i in range(2, num + 1):

        while True:
            if num % i == 0:
                # print(str(i) + "*", end='')
                tmp += i
                num = num / i
            else:
                break
    if (tmp + 1) == numOld:
        print(int(tmp + 1), numOld)
"""

for num in range(2, 1001):
    numOld = num;
    tmp = 0
    for i in range(1, num):
        if num % i == 0:
            tmp += i
    if tmp == num:
        print(num)

# encoding: utf-8
"""
【程序84】
题目：一个偶数总能表示为两个素数之和。
1.程序分析：
2.程序源代码：
"""
import math

odd = 98

li = []
for i in range(2, odd):
    flag = False
    for x in range(2, math.floor(math.sqrt(i)) + 1):
        if i % x == 0:
            flag = True
    if not flag:
        li.append(i)

print(li)

for i in li:
    for j in li:
        if i + j == odd:
            print(i, j)

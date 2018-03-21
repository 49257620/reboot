# encoding: utf-8
"""
【程序36】
题目：求100之内的素数　　　
1.程序分析：
2.程序源代码：
"""
import math
cnt = 0
for i in range(2, 101):
    flag = False
    for x in range(2, math.floor(math.sqrt(i)) + 1):
        if i % x == 0:
            flag = True
    if not flag:
        print(i)
        cnt += 1

print('total :', cnt)
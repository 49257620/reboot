# encoding: utf-8
"""
【程序12】
题目：判断101-200之间有多少个素数，并输出所有素数。
1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。 　　　　　　
2.程序源代码：
"""
import math

'''

print(math.sqrt(121))
for x in range(2, math.floor(math.sqrt(121))):
    print(121%x)

'''
cnt = 0
for i in range(101, 201):
    flag = False
    for x in range(2, math.floor(math.sqrt(i)) + 1):
        if i % x == 0:
            flag = True
    if not flag:
        print(i)
        cnt += 1

print('total :', cnt)

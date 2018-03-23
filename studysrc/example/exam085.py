# encoding: utf-8
"""
【程序85】
题目：判断一个数能被几个9整除
1.程序分析：
2.程序源代码：
"""

num = 90

cnt = 0

while num % 9 == 0 and num > 1:
    num /= 9
    cnt += 1

print(cnt)

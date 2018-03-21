# encoding: utf-8
"""
【程序25】
题目：求1+2!+3!+...+20!的和
1.程序分析：此程序只是把累加变成了累乘。
2.程序源代码：
"""
total = 0


def jiecheng(num):
    return 1 if num == 1 else num * jiecheng(num - 1)


# print(jiecheng(20))
for i in range(1, 21):
    total += jiecheng(i)
print(total)

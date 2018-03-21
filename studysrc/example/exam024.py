# encoding: utf-8
"""
【程序24】
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
1.程序分析：请抓住分子与分母的变化规律。
2.程序源代码：
"""


def getseq1(cnt):
    return 2 if cnt == 1 else (3 if cnt == 2 else (getseq1(cnt - 1) + getseq1(cnt - 2)))


def getseq2(cnt):
    return 1 if cnt == 1 else (2 if cnt == 2 else (getseq2(cnt - 1) + getseq2(cnt - 2)))


total = 0;

for i in range(1, 21):
    # print(str(getseq1(i)) + '/' + str(getseq2(i)))
    total += getseq1(i) / getseq2(i)

print(total)

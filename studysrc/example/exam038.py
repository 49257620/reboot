# encoding: utf-8
"""
【程序38】
题目：求一个3*3矩阵对角线元素之和
1.程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
2.程序源代码：：
"""
import random

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(a[0][0] + a[1][1] + a[2][2])


b= []

for i in range(3):
    b.append([])
    for j in range(3):
        b[i].append(random.randint(1,100))

sum = 0

for k in range(3):
    sum += b[k][k]

print(sum)
# encoding: utf-8
"""
【程序68】
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
1.程序分析：
2.程序源代码：
"""
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 5
ll = l[m:]

for x in l[0:m]:
    ll.append(x)
print(ll)



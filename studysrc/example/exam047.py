# encoding: utf-8
"""
【程序47】
题目：互相赋值　
1.程序分析：
2.程序源代码：

"""

a = 1
b = 2
c = 3
print(a, b)
a, b = b, a

a = 1
b = 2
c = 3
print(a, b, c)
a, b, c = b, c, a
print(a, b, c)

a = 1
b = 2
c = 3
print(a, b, c)
a, b, c = a + b, b + c, c + a
print(a, b, c)

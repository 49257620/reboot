# encoding: utf-8
"""
【程序76】
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数
　　　1/1+1/3+...+1/n(利用指针函数)
1.程序分析：
2.程序源代码：
"""


def plusn(n):
    return 1 / n if n <= 2 else 1 / n + plusn(n - 2)


print(plusn(99))

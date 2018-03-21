# encoding: utf-8
"""
【程序27】
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
1.程序分析：
2.程序源代码：
"""


def fn1(cnt):
    next = 0
    if cnt == 1:
        next = input('please input :')
        print(next)
    else:
        next = input('please input :')
        fn1(cnt - 1)
        print(next)


fn1(5)

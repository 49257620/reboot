# encoding: utf-8
"""
题目：输出9*9口诀。
1.程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
2.程序源代码：
"""
x = 1
y = 1

while x < 10:
    y = 1
    while y <= x:
        space = '';
        if x * y < 10:
            space = ' '
        print('%d*%d=%-2d' % (x, y, x * y), end=' ')
        y += 1
    print()
    x += 1

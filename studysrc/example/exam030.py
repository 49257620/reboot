# encoding: utf-8
"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。　　　
1.程序分析：同29例
2.程序源代码：
"""

num = 1123211
renum = ''
for c in reversed(str(num)):
    renum = renum + c

print('Y' if str(num) == renum else 'N')

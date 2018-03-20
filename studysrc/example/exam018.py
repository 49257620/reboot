# encoding: utf-8
"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时
　　　共有5个数相加)，几个数相加有键盘控制。
1.程序分析：关键是计算出每一项的值。
2.程序源代码：
"""

inputStr = '2'
times = int('5')
result = 0

for i in range(1, times + 1):
    result += int(str(inputStr) * i)

print(result)

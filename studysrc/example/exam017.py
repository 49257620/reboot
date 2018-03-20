# encoding: utf-8
"""
【程序17】
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
1.程序分析：利用while语句,条件为输入的字符不为'\n'.
　　　　　　
2.程序源代码：
"""
inputStr = 'AZazaaaa     1934123123~!++++'
alphaCnt = 0
spaceCnt = 0
numCnt = 0
othCnt = 0
total = 0

for c in inputStr:
    alphaCnt += (1 if (65 <= ord(c) <= 90) or (97 <= ord(c) <= 122) else 0)
    spaceCnt += (1 if ord(c) == 32 else 0)
    numCnt += (1 if 49 <= ord(c) <= 57 else 0)
    total += 1

print('共计:', total)
print('字母:', alphaCnt)
print('空格:', spaceCnt)
print('数字:', numCnt)
print('其它:', total - alphaCnt - spaceCnt - numCnt)

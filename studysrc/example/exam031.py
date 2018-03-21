# encoding: utf-8
"""
『程序31】
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续
　　　判断第二个字母。
1.程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
2.程序源代码
星期一： Mon.=Monday
星期二： Tues.=Tuesday
星期三： Wed.=Wednesday
星期四： Thur.=Thursday
星期五： Fri.=Friday
星期六： Sat.=Saturday
星期天： Sun.=Sunday
"""

str1 = 'T'
str2 = 'h'

list = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
list1 = []

for n, w in enumerate(list):
    if w[0] == str1:
        list1.append(n)

if list1.__len__() > 1:
    for i in list1:
        if str2 == list[i][1]:
            print(list[i])
else:
    print(list[(list1[0])])

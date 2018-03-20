# encoding: utf-8
"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。
2.程序源代码：
"""
import time

# print(time.strptime('20180305', '%Y%m%d'))

# print(time.asctime(time.strptime('20180305', '%Y%m%d')))

timeStr = input('输入日期格式YYYYMMDD:')
print(time.strftime("%Y-%m-%d", time.strptime(timeStr, '%Y%m%d')))
print('本年度第', int(time.strftime("%j", time.strptime(timeStr, '%Y%m%d'))), '天')

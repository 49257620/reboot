# encoding utf-8

year = int(input('输入年份:'))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(str(year) + '是闰年')
else:
    print(str(year) + '不是闰年')

# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’
"""
tell 方法针对中文字符一个字算三个位置，如果seek到中间会报错
seek方法针对文本文件只能从开始位置移动到后续位置，中间以及末尾位置只能移动到本身位置
针对二进制文件支持各种位置的前后移动
w 只支持写
r 只支持读
"""

f = open('C:\\PROJECTS\\Python\\tmpfile\\data4.txt', 'rt', encoding='utf-8')

print(f.read(5))
print(f.tell())

print(f.read(5))
print(f.tell())

f.seek(0, 0)
print(f.tell())
f.seek(10, 0)
f.seek(0, 1)
print(f.tell())
f.seek(0, 2)
print(f.tell())

f.close()

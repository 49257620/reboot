# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’
"""
rt+
针对文本方式，写入位置为末尾，以追加的形式
rb+
针对二进制方式打开，写入位置为当前指针位置，并且会覆盖掉相应字符

w+  会覆盖当前文件并清空,然后可以读写
x+ 会创建文件,如果文件存在则报错，并写入，如果已经存在会报错
a+ 会直接将指针放到末尾，无论在任何位置写入都会写入到末尾中
"""

# f = open('C:\\PROJECTS\\Python\\tmpfile\\data4.txt', 'r+', encoding='utf-8')
f = open('C:\\PROJECTS\\Python\\tmpfile\\data4.txt', 'rb+')

f.read(10)
# f.write(b"999")
f.write(b"999")
f.close()

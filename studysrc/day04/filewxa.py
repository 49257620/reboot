# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’

"""

w+  会覆盖当前文件并清空,然后可以读写
x+ 会创建文件,如果文件存在则报错，并写入，如果已经存在会报错,文本追加到末尾，二进制覆盖指针位置数据
a+ 会直接将指针放到末尾，无论在任何位置写入都会写入到末尾中
"""
"""
f = open('C:\\PROJECTS\\Python\\tmpfile\\data4.txt', 'a+')

f.read(3)

f.write(';;;')

f.close()



f = open('C:\\PROJECTS\\Python\\tmpfile\\data6.txt', 'x+')
f.write(':::::::::::::::::::::::::::')
f.write('>>>>>>>>>>>>>>>>>>>>>>>>>>>')


f.read(3)

f.write('???')

f.close()

"""

f = open('C:\\PROJECTS\\Python\\tmpfile\\data7.txt', 'xb+')
f.write(b':::::::::::::::::::::::::::')
f.write(b'>>>>>>>>>>>>>>>>>>>>>>>>>>>')

f.seek(0,0)
print(f.read(3))
print(f.tell())

f.write(b'???')

f.close()
# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’

"""

文件拷贝
创建1g文件 dd if=/dev/zero of=kk.txt bs=1M count=1000
"""

in_file = open('C:\\文档\\刘伟\\学习文档\Python\\01-Python基础入门.ppt', 'rb')

out_file = open('C:\\PROJECTS\\Python\\tmpfile\\01.ppt', 'wb')

while True:
    tmp = in_file.read(1024)
    if tmp == b'':
        break
    else:
        out_file.write(tmp)

in_file.close()
out_file.close()



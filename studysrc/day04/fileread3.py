# encoding: utf-8
# author = ‘LW’
"""
以二进制形式打开文本文件
二进制打开非文本尽量部用readline
"""

f = open('C:\\PROJECTS\\Python\\tmpfile\\data.txt', 'rb')

while True:
    tmp = f.read(3)

    if tmp == b'':
        break

    print(tmp)

f.close()

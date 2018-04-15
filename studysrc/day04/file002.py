# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’


f = open('C:\\PROJECTS\\Python\\tmpfile\\data.txt', 'rt',encoding='utf-8')

# print(f.read())

while True:
    tmp = f.read(3)

    if tmp == '':
        break

    print(tmp)

f.close()
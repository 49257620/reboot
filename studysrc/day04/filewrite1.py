# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’


f = open('C:\\PROJECTS\\Python\\tmpfile\\中文名称测试.txt', 'wt', encoding='utf-8')

f.write("中文测试")
f.write("True")
f.write(str((1, 2, 3, 4, 5)))
f.write(str({'name': 'liuwei'}))

f.close()

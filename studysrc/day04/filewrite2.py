# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’
"""

write lines  不会自动加换行
"""

f = open('C:\\PROJECTS\\Python\\tmpfile\\data3.txt', 'wt', encoding='utf-8')

f.writelines(["中文测试\n", '1223123123\n', 'asdasdasdasdasd'])

f.close()

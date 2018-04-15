# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’
"""
x
文件存在的情况下报错
文件部存在的情况下创建并写入
"""

f = open('C:\\PROJECTS\\Python\\tmpfile\\data4.txt', 'xt', encoding='utf-8')

f.writelines(["中文测试\n", '1223123123\n', 'asdasdasdasdasd'])

f.close()

# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’
"""
a
文件存在的情况下追加写入
文件部存在的情况下创建并写入
"""

f = open('C:\\PROJECTS\\Python\\tmpfile\\data4.txt', 'at', encoding='utf-8')

f.writelines(["\nnn中文测试\n", 'nn1223123123\n', 'nnasdasdasdasdasd'])

f.close()

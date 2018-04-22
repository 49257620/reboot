# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


age = '30'

age = int(age) if age.isdigit() else 18

print(age)

age = 'aaa'
# a and b or c
# 如果a成立则返回b，否则返回c
age = age.isdigit() and int(age) or 18

print(age)


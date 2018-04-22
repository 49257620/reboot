# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


def fun_param(name, age=0):
    print('I am %s ,I am %d years old.' % (name, age))


fun_param('ll')
fun_param(name='ll', age=30)
fun_param('ll', age=30)
# fun_param(name='ll', 30)
fun_param(age=30, name='ll')


def fun_param_list(namelist=[]):
    print(namelist.pop())


fun_param_list([1, 2, 3, 4, 5])


# 列表形式参数
def fun_param1(*args):
    print(args)


fun_param1('aa', 10, 'nan')


# 字典形式参数
def fun_param2(title,content,*args,**kwargs):
    print(title)
    print(content)
    print(args)
    print(kwargs)


fun_param2(1,2,3,4,5,name='aa', age=10, sex='nan')

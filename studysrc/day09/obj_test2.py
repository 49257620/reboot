# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
'''
类的属性和实例的属性可以动态赋值
在访问实例属性时，优先访问实例的属性，当实例属性不存在时则访问类的属性，若类属性值不存在，则报错
设置&修改实例的属性值，不影响类的属性值
'''


class Dog(object):
    pass


if __name__ == '__main__':
    # 定义Dog的属性name和age，初始化为'dog' 和 0
    print('定义Dog的属性name和age，初始化为dog 和 0')
    Dog.name = 'dog'
    Dog.age = 0
    wangwang = Dog()
    doudou = Dog()

    print('-' * 20)

    # 访问Dog、wangwang、doudou的name和age属性
    print('访问Dog、wangwang、doudou的name和age属性')
    print('访问Dog的name和age属性:', Dog.name, Dog.age)
    print('访问wangwang的name和age属性:', wangwang.name, wangwang.age)
    print('访问doudou的name和age属性:', doudou.name, doudou.age)

    print('-' * 20)
    # 设置wangwang的name和age属性，访问Dog、wangwang和doudou的name和age属性
    print('设置wangwang的name和age属性，访问Dog、wangwang和doudou的name和age属性')
    wangwang.name = 'wangwang'
    wangwang.age = 10
    print('访问Dog的name和age属性:', Dog.name, Dog.age)
    print('访问wangwang的name和age属性:', wangwang.name, wangwang.age)
    print('访问doudou的name和age属性:', doudou.name, doudou.age)

    print('-' * 20)
    print('修改Dog的name和age属性为’dogdog’和2，访问Dog、wangwang和doudou的name的age属性')
    Dog.name = 'dogdog'
    Dog.age = 2
    print('访问Dog的name和age属性:', Dog.name, Dog.age)
    print('访问wangwang的name和age属性:', wangwang.name, wangwang.age)
    print('访问doudou的name和age属性:', doudou.name, doudou.age)

    print('-' * 20)
    print('设置doudou的sex为1，访问Dog、wangwnag、 doudou的sex属性')
    doudou.sex = 1
    print('访问doudou的sex属性:', doudou.sex)
    print('访问Dog的sex属性:', Dog.sex)  # 报错
    print('访问wangwang的sex属性:', wangwang.sex)  # 报错

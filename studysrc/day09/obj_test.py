# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


class Person(object):
    pass


if __name__ == '__main__':
    lw = Person()

    # 实例的属性
    lw.name = 'liuwei'
    lw.age = 33

    # 类的属性
    Person.height = 0.3

    # 实例的属性
    print('实例的属性:name: ', lw.name)
    print('实例的属性:age: ', lw.age)

    # 类的属性
    print('实例没有height属性，直接找类的属性')
    print('类的属性:Person：height: ', Person.height)
    print('类的属性:lw：height: ', lw.height)

    # 实例属性重新赋值
    print('实例属性重新赋值 lw.height = 1.68')
    lw.height = 1.68
    print('类的属性变了:lw：height: ', lw.height)
    print('类的属性不变:Person：height: ', Person.height)


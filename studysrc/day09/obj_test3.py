# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


class Person(object):
    name = ''
    age = 0


if __name__ == '__main__':
    lw = Person()

    # 类的属性
    print('类的属性')
    print('类的属性:Person：name: ', Person.name)
    print('类的属性:Person: age: ', Person.age)

    # 实例的属性
    print('实例的属性未赋值时使用实例的属性')
    print('实例的属性:name: ', lw.name)
    print('实例的属性:age: ', lw.age)






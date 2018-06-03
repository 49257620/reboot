# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


class Person(object):
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    lw = Person('liuwei', 35)
    kk = Person('kk', 30)

    print('lw:', lw.name, lw.age)
    print('kk:', kk.name, kk.age)

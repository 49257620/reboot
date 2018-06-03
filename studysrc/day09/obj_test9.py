# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


class Person(object):
    __slots__ = ("__name", "__age")
    id = 0

    # 构造函数
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 类方法装饰器 @classmethod
    @classmethod
    def gen_id(cls):
        cls.id += 1
        return cls.id

    # 静态方法  @staticmethod
    @staticmethod
    def static_test(txt):
        print(txt)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


if __name__ == '__main__':
    lw = Person('lw', 30)

    print(lw.name)
    lw.name = 'kk'

    print(lw.name)

    lw.age =10

    print(lw.name)
    print(lw.age)

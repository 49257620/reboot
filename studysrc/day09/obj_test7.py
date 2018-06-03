# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


class Person(object):
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

    # 实例的方法
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


if __name__ == '__main__':
    lw = Person('lw',30)

    print(lw.get_name())
    lw.age = 10
    print(lw.get_age())
    print(lw.age)

# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


class Person(object):
    __slots__ = ("name", "age")
    id = 0

    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

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
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


if __name__ == '__main__':
    lw = Person('lw',30)

    lw.name = 'kk';
    print(lw.get_name())
    lw.sex = 1

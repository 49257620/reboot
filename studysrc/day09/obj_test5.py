# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


class Person(object):
    name = ''
    age = 0
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
    print('调用类方法：')
    print(Person.gen_id())

    lw = Person('ll', 20)
    print('调用实例方法：')
    print(lw.get_name())
    print('设置name的值,然后再次调用实例的方法 ：')
    lw.set_name("ww")
    print(lw.get_name())

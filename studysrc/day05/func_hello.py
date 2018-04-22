# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


def say_hello():
    print('Hello KK')


say_hello()


print(say_hello, id(say_hello))


def return_tuple():
    print('return tuple')
    return (1, 2, 3, 4), (12345)


s = return_tuple()

print(s)

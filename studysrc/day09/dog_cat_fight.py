# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

import random


class Dog(object):

    def __init__(self, name, blood=100):
        self.name = name
        self.blood = blood

    def get_blood(self):
        return self.blood

    def drop_blood(self, drop):
        self.blood -= drop
        print(self.name, '损失了', drop, '血量，剩余', self.blood)

    def attack(self, rival):
        print(self.name, '发起了攻击：', end='')
        rival.drop_blood(random.randint(0, 20))


class Cat(object):

    def __init__(self, name, blood=100):
        self.name = name
        self.blood = blood

    def get_blood(self):
        return self.blood

    def drop_blood(self, drop):
        self.blood -= drop
        print(self.name, '损失了', drop, '血量，剩余', self.blood)

    def attack(self, rival):
        print(self.name, '发起了攻击：', end='')
        rival.drop_blood(random.randint(0, 20))


def start_fight(first, second):
    idx = 0
    while first.get_blood() > 0 and second.get_blood() > 0:
        if idx % 2 == 0:
            first.attack(second)
        else:
            second.attack(first)
        idx += 1

    if first.get_blood() > 0:
        print(first.name, '赢了，剩余', first.blood)
    else:
        print(second.name, '赢了，剩余', second.blood)


if __name__ == '__main__':
    wangwang = Dog('wangwang')
    miaomiao = Cat('miaomiao', 120)

    start_fight(wangwang, miaomiao)

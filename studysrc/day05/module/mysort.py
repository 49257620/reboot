# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


def fun_bubble(li, key=lambda x: x):
    length = len(li)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if key(li[j]) > key(li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]


if __name__ == '__main__':
    print('fun_bubble main')

# print('fun_bubble name', __name__)

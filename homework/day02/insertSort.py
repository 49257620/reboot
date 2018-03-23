# encoding: utf-8
"""
作业1：插入排序算法

"""
a = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

print('before sort: ', a)


def insert_sort(li):
    for i in range(1, len(li)):
        j = i
        while j > 0 and li[j] < li[j - 1]:
            li[j], li[j - 1] = li[j - 1], li[j]
            j -= 1
    return li


insert_sort(a)

print('after sort: ', a)

# encoding: utf-8
# author = ‘LW’


def josephus_fun(total, step):
    my_list = [x + 1 for x in range(total)]

    while len(my_list) > 1:
        tmp = my_list[:step-1]
        my_list = my_list[step:]
        my_list.extend(tmp)

    print('剩余人为：', my_list[0])


josephus_fun(9, 2)

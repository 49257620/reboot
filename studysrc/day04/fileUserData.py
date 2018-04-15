# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’
"""
将数据保存到文件 fileUserData.dat
每条数据一行
读取文件，并还原成数据，打印出来

"""

def save_users():
    users = {
        1: {'name': '刘伟1', 'age': 31, 'tel': '158xxxx1'},
        2: {'name': '刘伟2', 'age': 32, 'tel': '158xxxx2'},
        3: {'name': '刘伟3', 'age': 33, 'tel': '158xxxx3'},
    }

    save_file = open('fileUserData.dat', 'wt', encoding='utf-8')

    for key, value in users.items():
        user = str(key) + ',' + value['name'] + ',' + str(value['age']) + ',' + value['tel'] + '\n'
        save_file.write(user)

    save_file.close()


def read_users():
    users = {}
    read_file = open('fileUserData.dat', 'rt', encoding='utf-8')

    for line in read_file:
        user = line.split(',')
        users[int(user[0])] = {'name': user[1], 'age': int(user[2]), 'tel': user[3].strip()}

    read_file.close()
    print(users)

# save_users()
read_users()

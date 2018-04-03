# encoding: utf-8
# Author: LW

# 初始化用户清单
users = {
    4: {'name': 'kk1', 'age': 28, 'tel': '158xxxxx'},
    2: {'name': 'kk15', 'age': 29, 'tel': '168xxxxx'},
    3: {'name': 'kk3', 'age': 30, 'tel': '178xxxxx'},
    1: {'name': 'kk4', 'age': 31, 'tel': '158xxxxx'}
}

title = ('Id', 'Name', 'Age', 'Tel')
format_title = '|{0[0]:^10s}|{0[1]:^20s}|{0[2]:^10s}|{0[3]:^24s}|'
title_str = format_title.format(title)

format_str = '|{0[0]:^10d}|{0[1][name]:^20s}|{0[1][age]:^10d}|{0[1][tel]:^24s}|'

print((1,users.get(1)))

user_temp = {'name': 'kk5', 'age': 31, 'tel': '158xxxxx'}

print(users)

def check_name_exist(id, name):
    is_exist = False
    for key , user in users.items() :
        if key == id:
            continue
        else:
            if user.get('name') == name:
                is_exist = True
                break
    return is_exist


def search_user(conditions):
    search_users_list  = {}
    for key , user in users.items() :
        if user.get('name').find(conditions.strip()) != -1 or user.get('tel').find(conditions.strip()) != -1:
            search_users_list[key] =  user

    return search_users_list


print (search_user('15'))

users_list  = []
for k,v in users.items():
    users_tuple = (k,v.get('name'),v.get('age'),v.get('tel'))
    users_list.append(users_tuple)

print(sorted(users_list, key=lambda s: s[0]))
print(users_list)
print(list(users.values()))
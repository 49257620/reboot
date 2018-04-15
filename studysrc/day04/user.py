# encoding: utf-8

users = {}

tpl = '|{uid:10d}|{name:10s}|{age:5d}|{tel:20s}|'

while True:
    operate = input('请输入操作(add/delete/update/find/list):')
    if 'add' == operate:
        text = input('请输入用户信息(示例:kk,30,152xxxxxxxx):')
        nodes = text.split(',')
        if len(nodes) != 3:
            print('输入信息有误, 请重新进行操作')
        else:
            if not nodes[1].isdigit():
                print('输入年龄有误，请重新进行操作')
            else:
                uid = 1
                if users:
                    uid = max(users) + 1

                users[uid] = {
                    'name': nodes[0],
                    'age': int(nodes[1]),
                    'tel': nodes[2]
                }
                print('添加用户成功')
    elif 'delete' == operate:
        uid = input('请输入删除用户ID:')
        if not uid.isdigit():
            print('输入信息有误')
        else:
            user = users.pop(int(uid), None)
            if user:
                print('删除成功')
            else:
                print('删除失败，用户信息不存在')
    elif 'update' == operate:
        uid = input('请输入编辑用户ID:')
        if not uid.isdigit() or int(uid) not in users:
            print('输入信息有误')
        else:
            text = input('请输入用户信息(示例:30,152xxxxxxxx):')
            nodes = text.split(',')
            if len(nodes) != 2:
                print('输入信息有误, 请重新进行操作')
            else:
                if not nodes[0].isdigit():
                    print('输入年龄有误，请重新进行操作')
                else:
                    users[int(uid)]['age'] = nodes[0]
                    users[int(uid)]['tel'] = nodes[1]

                    users[int(uid)] = {
                        'name': users[int(uid)]['name'],
                        'age': nodes[0],
                        'tel': nodes[1]
                    }
                    print('更改成功')
    elif 'list' == operate:
        for key, value in users.items():
            print(tpl.format(uid=key, name=value['name'], age=value['age'], tel=value['tel']))
    elif 'find' == operate:
        text = input('请输入查询的字符串:')
        for key, value in users.items():
            if text in value['name']:  # if value['name'].find(text) != -1:
                print(tpl.format(uid=key, name=value['name'], age=value['age'], tel=value['tel']))

# 增
# 让用户输入信息(name, age, tel) => input()
# woniu,30,185xxxxxxxx => split(',') => list => name, age, tel
# 检查元素数量,类型
# 检查失败，提示用户
# max(users) => +1
# users[id] = {'name' : name, 'age' : int(age), 'tel' : tel}
# 提示成功
# 删
# 让用户输入删除的ID
# 检查 ID是否存在
# 检查失败，提示用户
# 打印用户信息，并询问是否删除
# 真删除
# 删除del, pop
# 提示成功
# 改
# 让用户输入修改的ID
# 检查ID是否存在
# 检查失败, 提示用户
# 让用户输入需要修改后的信息
# woniu,30,185xxxxxxxx => split(',') => list => name, age, tel
# 检查元素数量,类型
# 检查失败，提示用户
# 检查成功, users[id]['name'] = name, users[id] = {}
# 提示用户成功

# 查
# 让用户输入查找内容
# for key, value in users
# value['name'].find() in
# format

# 列表
# for key, value in users
# format 占位 {0} {name}

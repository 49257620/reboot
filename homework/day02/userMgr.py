# encoding: utf-8
# Author: LW
"""
用户管理功能说明：
    A.显示欢迎信息
        *********************************************************************
        *                     Welcome to User Management                    *
        *        You can select a menu number to choose an operation        *
        *********************************************************************
    B.初始化用户信息
        ---------------------------------------------------------------------
        |    Id    |        Name        |   Age    |          Tel           |
        ---------------------------------------------------------------------
        |    1     |      Liu Wei       |    29    |      18500000001       |
        |    2     |       Li Si        |    28    |      18600000002       |
        |    3     |       Zh San       |    30    |      18700000003       |
        ---------------------------------------------------------------------
    C.通过屏幕显示菜单
        -	1. List Users. （用户列表）
        -	2. Add User.   （增加用户）
        -	3. Delete User.（删除用户）
        -	4. Edit User.  （修改用户）
        -	5. Find User.  （查找用户）
        -	0. Exit System.（推出系统）
    D.用户通过命令行输入相关的菜单ID，进入相关的功能
        1.用户列表：
            - 输出全部用户列表到屏幕
                - 如果列表中没有数据，则提示用户：没有数据！
            - 直接回车返回菜单选择画面
        2.增加用户：
            - 提示用户输入增加的用户信息（Name,Age,Tel）
            - 获取当前用户列表中最大的ID值，并加1 ，最为新用户的ID
            - 将新用户插入到用户列表中
            - 增加后提示成功，并回车返回菜单选择画面
        3.删除用户：
            - 显示全部用户列表，以便用户选择要删除的对象
            - 用户输入要删除的记录ID
                - ID不存在：返回菜单
                - ID存在：将用户选择的记录显示在屏幕上，并要求用户确认删除
                    - 输入'非Y'：返回菜单
                    - 输入'Y'：将记录从users list中移除
            - 删除后提示成功，并回车返回菜单选择画面
        4.修改用户
            - 显示全部用户列表，以便用户选择要修改的对象
            - 用户输入要修改的ID
                - 如用户输入的ID 不存在则返回菜单
                - 如用户输入的ID存在，将要修改的记录显示在屏幕中，并提示用户输入（Name,Age,Tel）
            - 修改后提示成功，并回车返回菜单选择画面
        5.查找用户
            - 提示用户输入姓名
            - 根据姓名查找users list
                - 如有数据：显示相关信息
                - 无数据：提示无数据，并返回菜单
    E.退出系统
        *********************************************************************
        *                 Good Bye and see you next time!                   *
        *********************************************************************
    F.未完成事项
        - TODO 注释的部分为应该处理，但是实际未进行处理的部分，需要稍后补充，
          主要包括相关输入的合法性验证
        - 程序进入菜单后，再次输入的部分，一旦输入错误则直接返回菜单，此处不合理
          应在进入菜单分支后使用 while循环，一旦输入错误，需返continue后重新输入
          由于时间有限此部分尚未实现
        - 未对ID，姓名，电话等字段的重复性进行验证，也未验证用户输入的参数长度是否
          合法，需实现
        - 现阶段仅将 列表显示（print_user_list()），单个用户显示（print_user(user)），
          打印菜单（print_menu()）部分定义了函数，应将其他可以抽象的部分都以函数的形
          式重新整理，增加代码的可读性。
"""

#  打印初始化信息
print('*********************************************************************')
print('*                     Welcome to User Management                    *')
print('*        You can select a menu number to choose an operation        *')
print('*********************************************************************')

# 初始化用户清单
users = [(1, 'Liu Wei', 29, '18500000001'), (2, 'Li Si', 28, '18600000002'), (3, 'Zh San', 30, '18700000003')]
# 初始化列表标题
title = ('Id', 'Name', 'Age', 'Tel')
# 定义列表模板，注意此处使用的是元组作为参数{0},元组中的元素使用0[0](Id)，0[1](Name)，0[2](Age)，0[3](Tel)表示，以便参数传递
format_str = '|{0[0]:^10d}|{0[1]:^20s}|{0[2]:^10d}|{0[3]:^24s}|'
# 定义列表标题，注意此处使用的是元组作为参数{0},元组中的元素使用0[0](Id)，0[1](Name)，0[2](Age)，0[3](Tel)表示，以便参数传递
format_title = '|{0[0]:^10s}|{0[1]:^20s}|{0[2]:^10s}|{0[3]:^24s}|'
# 将title元组直接进行格式转换
title_str = format_title.format(title)
# 定义分割线
split_line = '-' * len(title_str)


# 打印菜单方法
def print_menu():
    # 以下在屏幕上直接输出与定义的菜单
    # 采用此方式是为了避免用户输入过多内容可能引起的输入错误
    # 用户通过输入菜单编号访问相关功能，既方便又能减少失误
    print('---------------------------Menu List---------------------------------')
    print("-\t1. List Users.")
    print("-\t2. Add User.")
    print("-\t3. Delete User.")
    print("-\t4. Edit User.")
    print("-\t5. Find User.")
    print("-\t0. Exit System.")
    print('---------------------------------------------------------------------')


# 打印全部用户列表方法
def print_user_list():
    # 打印分割线
    print(split_line)
    # 打印列表标题行
    print(title_str)
    # 打印分割线
    print(split_line)
    # 如果users list 中有记录，则遍历users list ，逐条输出到屏幕上
    if len(users) > 0:
        # 遍历users list
        for i in users:
            # 逐行使用模板 进行format 输出
            print(format_str.format(i))
    # 如果users list中无记录，则直接输出一行'no user yet!' 提示用户没有相关记录
    else:
        print('                   no user yet!')
    # 打印分割线
    print(split_line)


# 打印单个用户方法
def print_user(user):
    # 打印分割线
    print(split_line)
    # 打印列表标题行
    print(title_str)
    # 打印分割线
    print(split_line)
    # 根据传入的参数user对象，打印一行数据
    print(format_str.format(user))
    # 打印分割线
    print(split_line)


while True:
    # 进入循环，首先打印菜单列表
    print_menu()
    # 用户输入菜单ID，判断用户输入是否为数字，如果不是数字提示输入错误重新输入
    try:
        operation_code = int(input('请输入菜单序号，选择需要进行的操作：'))
    except ValueError as e:
        # 捕获int转换异常，重新开始循环
        print('输入错误，请重新输入：')
        continue
    # 选择0，则退出，打印退出信息
    if operation_code == 0:
        print('*********************************************************************')
        print('*                 Good bye and see you next time!                   *')
        print('*********************************************************************')
        break
    # 选择1，进入列表
    elif operation_code == 1:
        # 打印列表到屏幕，提示用户输入任意键返回菜单画面
        print_user_list()
        input('任意输入按下回车返回菜单：')
    # 选择2，进入增加用户功能
    elif operation_code == 2:
        # 用户输入数据，格式为Name,Age,Tel，
        # TODO 未对用户输入的内容做合法性验证，稍后需补充
        insert_info = input('请输入增加的用户信息（Name,Age,Tel）：')
        # 用户输入的数据，使用','进行分解成list对象，放入临时对象insert_user_tmp中
        insert_user_tmp = insert_info.split(',')
        # 将age字段类型强制转换成 int，统一age类型
        insert_user_tmp[1] = int(insert_user_tmp[1])
        # 定义最大ID号变量，并初始化值为 0 ，用于循环遍历比较
        max_id = 0
        # 遍历 用户 list，如果用户的id大于max_id,则将 用户id赋值给 max_id
        # 最终获得最大的用户ID
        for user in users:
            if user[0] > max_id:
                max_id = user[0]
        # 获得新tuple对象insert_user，由 max_id+1作为ID，用户输入的部分直接apend到ID后面
        insert_user = (max_id + 1,) + tuple(insert_user_tmp)
        # 将新用户对象直接append到用户list中
        users.append(insert_user)
        # 在屏幕输出新添加的用户信息
        print_user(insert_user)
        # 提示用户添加成功，任意输入按下回车返回菜单
        input('用户添加成功，任意输入按下回车返回菜单：')
    # 选择3，进入删除用户功能
    elif operation_code == 3:
        # 首先输出用户清单到屏幕，以便用户选择对应要删除的ID
        print_user_list()
        # 用户输入要删除的用户ID，判断用户输入是否为数字，如果不是数字提示输入错误重新输入
        try:
            delete_next = int(input('请输入要删除的用户ID：'))
        except ValueError as e:
            # 捕获int强制转换错误，如果输入的不是数字则直接返回菜单，重新选择
            print('输入错误，请重新输入：')
            continue
        # 定义要删除的user对象 delete_user 稍后使用
        delete_user = None
        # 根据用户输入的ID 获取要删除的user list （因为ID 未做唯一性的验证，所以可能存在多行所以为list对象）
        delete_user_list = list((x for x in users if x[0] == delete_next))
        # 判断要删除的对象是否存在，如果list长度大于0 ，则表示存在相关ID的用户
        if len(delete_user_list) > 0:
            # 此处仅获取第一条作为要删除的对象，赋值给 delete_user
            delete_user = delete_user_list[0]
            # 将要删除的对象输出到屏幕上，以便用户确认删除数据信息
            print_user(delete_user)
            # 提示用户是否确认删除，如果要删除，输入Y回车，否则返回菜单
            delete_confirm = input('上方为要删除的用户信息，确认删除请输入Y，否则直接输入回车返回菜单：')
            # 用户输入'Y'，确认删除记录
            if delete_confirm == 'Y':
                # user list中将要删除的对象 remove
                users.remove(delete_user)
                # 提示用户删除成功，同时提示任意输入按下回车返回菜单
                input('用户：' + delete_user[1] + ' 删除成功，任意输入按下回车返回菜单：')
        else:
            # 如果list长度小于等于0 ，则表示未找到相关用户信息，直接提示用户未找到，并提示返回
            input('未找到相关用户信息，任意输入按下回车返回菜单：')
    # 选择4，进入修改用户功能
    elif operation_code == 4:
        # 首先输出用户清单到屏幕，以便用户选择对应要修改的ID
        print_user_list()
        # 用户输入要修改的用户ID，判断用户输入是否为数字，如果不是数字提示输入错误重新输入
        try:
            edit_next = int(input('请输入要修改的用户ID：'))
        except ValueError as e:
            # 捕获int强制转换错误，如果输入的不是数字则直接返回菜单，重新选择
            print('输入错误，请重新输入：')
            continue
        # 定义要修改的user对象 edit_user 稍后使用
        edit_user = None
        # 根据用户输入的ID 获取要修改的user list （因为ID 未做唯一性的验证，所以可能存在多行所以为list对象）
        edit_user_list = list((x for x in users if x[0] == edit_next))
        # 判断要修改的对象是否存在，如果list长度大于0 ，则表示存在相关ID的用户
        if len(edit_user_list) > 0:
            # 此处仅获取第一条作为要修改的对象，赋值给 edit_user
            edit_user = edit_user_list[0]
            # 将要修改的对象输出到屏幕上，以便用户确认删除数据信息
            print_user(edit_user)
            # 提示用户修改方式 输入 Name,Age,Tel 以便修改上方显示的用户信息，ID不能修改
            # TODO 未对用户输入的内容做合法性验证，稍后需补充
            edit_info = input('上方为要修改的用户信息，请输入修改信息（Name,Age,Tel）：')
            # 用户输入的数据，使用','进行分解成list对象，放入临时对象mod_user中
            mod_user = edit_info.split(',')
            # 将age字段类型强制转换成 int，统一age类型
            mod_user[1] = int(mod_user[1])
            # 将用户ID 以及用户输入的内容转换成新的 tuple对象，并赋值给原对象
            # users[users.index(edit_user)] 首先使用index访问获取原对象的索引，
            # 再使用 users[原对象索引] 获取对象并直接赋值
            # 使用这种方式而不是先remove 再append 的原因是可以保持修改对象的位置不发生变化
            users[users.index(edit_user)] = (edit_user[0],) + tuple(mod_user)
            # 提示修改成功，并任意输入按下回车返回菜单
            input('用户Id：' + str(edit_user[0]) + ' 修改成功，任意输入按下回车返回菜单：')
        else:
            # 如果list长度小于等于0 ，则表示未找到相关用户信息，直接提示用户未找到，并提示返回
            input('未找到相关用户信息，任意输入按下回车返回菜单：')
    # 选择5，进入查找用户功能
    elif operation_code == 5:
        # 输入要查找的用户名
        find_next = input('请输入用户姓名：')
        # 根据用户输入的姓名 对 users list进行查找，获取查找结果find_user_list
        find_user_list = list((x for x in users if x[1] == find_next))
        # 如果find_user_list 长度大于0 ，则表示查找到了匹配的记录
        if len(find_user_list) > 0:
            # 如果查找到了记录，则打印到屏幕
            # TODO 此处可以遍历find_user_list，将所以查找的到记录全部输入到屏幕上，由于懒尚未实现，仅输出了第一条
            print_user(find_user_list[0])
            # 提示用户返回菜单
            input('任意输入按下回车返回菜单：')
        # 否则 ，则表示未能查找到匹配的记录
        else:
            # 未找到匹配记录的情况下，给出提示
            input('未找到相关用户信息，任意输入按下回车返回菜单：')
    else:
        # 输入不存在的菜单ID的情况下，提示错误，退出当前循环，重新开始。
        print('输入错误，请重新输入：')
        continue

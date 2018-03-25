# encoding: utf-8
# author = ‘LW’
"""
提示用户输入do或者任务(非do)
如果用户输入任务，则添加到list中
如果用户输入do，当任务为空时则打印无任务并退出，否则从list中根据先进先出原则打印任务

"""

todo_list = ['aa', 'bb', 'cc']

while True:
    thing = input("输入do或者任务(非do):")
    if thing == 'do':
        if todo_list:
            print('完成任务：', todo_list.pop(0))
        else:
            print('今天任务已完成')
            break
    else:
        todo_list.append(thing)
        print('增加任务：', thing)



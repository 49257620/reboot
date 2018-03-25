# encoding: utf-8
# author = ‘LW’

users = []

users.append((1, 'Liu Wei', 29, '18500000001'))
users.append((2, 'Li Si', 28, '18600000002'))
users.append((3, 'Zhang S', 30, '18700000003'))

title = ('Id', 'Name', 'Age', 'Tel')
'''
format_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
format_str = '|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'
title_str = format_title.format(title[0], title[1], title[2], title[3])
print('-' * len(title_str))
print(title_str)
print('-' * len(title_str))

for i in users:
    print(format_str.format(i[0], i[1], i[2], i[3]))

print('-' * len(title_str))

print('*' * 50)
'''
format_title_2 = '|{0[0]:^10s}|{0[1]:^10s}|{0[2]:^5s}|{0[3]:^15s}|'
format_str_2 = '|{0[0]:^10d}|{0[1]:^10s}|{0[2]:^5d}|{0[3]:^15s}|'
title_str_2 = format_title_2.format(title)
split_line = '-' * len(title_str_2)
print(split_line)
print(format_title_2.format(title))
print(split_line)
for i in users:
    print(format_str_2.format(i))

print(split_line)

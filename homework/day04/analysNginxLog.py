# encoding: utf-8
# Author: LW

log_file = open('E:\\个人资料\\Python\\logs\\access.txt', 'rt')
log_static = {}

for line in log_file:
    line_info = line.split()
    if line_info[8] == '200':
        log_static[(line_info[0], line_info[6], line_info[8])] = log_static.setdefault(
            (line_info[0], line_info[6], line_info[8]), 0) + 1
        log_static.setdefault((line_info[0], line_info[6], line_info[8]), 1)

log_file.close()
log_static_sort = []

for k, v in log_static.items():
    # log_static_sort.append(list(k).append(v))
    ttt = list(k) + [v]
    log_static_sort.append(ttt)

log_static_sort = sorted(log_static_sort, key=lambda s: s[3], reverse=True)

format_title = '|{0[0]:^20s}|{0[1]:^50s}|{0[2]:^5s}|{0[3]:^5s}|'
format_str = '|{0[0]:^20s}|{0[1]:^50s}|{0[2]:^5s}|{0[3]:^5d}|'
title = format_title.format(['IP', 'URL', 'CODE', 'CNT'])

result_file = open('E:\\个人资料\\Python\\logs\\access_result.txt', 'wt')

result_file.write(title + '\n')
result_file.write('-' * len(title) + '\n')
for x in range(10):
    result_file.write(format_str.format(log_static_sort[x]) + '\n')

result_file.close()

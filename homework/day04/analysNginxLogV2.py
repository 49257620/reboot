# encoding: utf-8
# Author: LW


"""
import time
tt =  bbb[3][2:] # '3/Aug/2014:00:01:42'
time.strptime(tt,"%d/%b/%Y:%H:%M:%S")

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""

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

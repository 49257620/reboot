# encoding: utf-8
# author = ‘LW’
"""
文件可以遍历，每个元素为一行

"""
f = open('C:\\PROJECTS\\Python\\tmpfile\\data.txt', 'rt', encoding='utf-8')

for line in f:
    print(line, end='')

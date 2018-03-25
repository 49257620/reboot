# encoding: utf-8
# author = ‘LW’
"""
str 方法：
1. split
    S.split(sep=None, maxsplit=-1) -> list of strings
2. format
"""
# split
print('无分割：', 'abc'.split())
print('空格分割：', 'a d c e f'.split())
print('字母d分割：', 'a d c e f'.split('d'))
print('","分割：', 'aa,bb,cc,dd,1,2,3,4'.split(','))

# format

print('我的名字是：' + 'll' + ',我的年龄：' + str(30))
print('我的名字是：{0} ,我的年龄：{1}'.format('ll', 30))
print('我的名字是：{1} ,我的年龄：{0}'.format('ll', 30))
print('我的名字是：{1} ,我的年龄：{0}-{1}'.format('ll', 30))
print('我的名字是：{0} ,我的年龄：{1:5.2f}'.format('ll', 30))
print('我的名字是：{0} ,我的年龄：{1:04d}'.format('ll', 30))
print('我的名字是：{0} ,我的年龄：{1:0<4d}'.format('ll', 30))
print('我的名字是：{0} ,我的年龄：{1:0^4d}'.format('ll', 30))

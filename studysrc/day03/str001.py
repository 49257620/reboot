# encoding: utf-8
# author = ‘LW’

chars = 'abcdefghijklmnopqrstuvwxyz'
nums = '123456789'

# 可遍历
'''
for ch in chars:
    print(ch)
'''

# 四则运算

chars_1 = chars + chars
chars_2 = chars * 3

print(chars_1, chars_2)

# len max  min
print('len:', len(chars))
print('max:', max(chars))
print('min:', min(chars))
# print('sum:',sum(nums)) 即使均为数字也不能用sum

# 切片

print('倒序：', chars[::-1])
print('隔行：', chars[::2])

print('{0:>3s}{1}'.format('a', 'b'))

# count index find
print('count a:', chars.count('a'))
print('count abc:', chars.count('abc'))
# index 不存在时报错
print('index z:', chars.index('z'))
print('index xyz:', chars.index('xyz'))
print('find:', chars.find('A'))

# encode 转换成二进制字符串
print('我是KK'.encode())

# format s-> 字符串 d -> 数字 f -> 浮点型
print('format:{0:>3s}---{1}---{2:^10.2f}-{2:>10.2f}-{2:<10.2f}--{{aaa{1}}}'.format('a', 'b', 1.68))

print('format2 : {name:s}说：我是{name},我的身高是{height:5.2f}'.format(name='kk', height=1.68))

# startswith endswith
print('startswith:', chars.startswith("abc"))
print('endswith true:', chars.endswith("abc"))
print('endswith false:', chars.endswith("xyz"))
print('find start:', chars.find("abc"))
print('find end:', chars.find("xyz"))

# isxxxxxx
print('is alnum', '123abc'.isalnum())
print('is isalpha', 'abc'.isalpha())
print('is isdigit', '123'.isdigit())
print('is isidentifier', 'print'.isidentifier())
print('is isspace', '   '.isspace())

# title
print('title:', 'abc efg'.title())

# split
print('split:', 'abcd\r\nefg'.split())
print('splitlines:', 'abcd\r\nefg'.splitlines())

# join 参数为可遍历对象
print('join:', '.'.join(['192', '168', '1', '1']))
print('join:', '_'.join(['192', '168', '1', '1']))

# replace
chars *= 2
print('replace : ', chars.replace('abc', '123'))
print('replace : ', chars.replace('abc', '9', 1))

print(chars.rfind('xyz'))

# 找第二个ab的位置
chars = 'abcedfabce'


idx = chars.find('ab')
print(idx)
print(chars.find('ab', idx+1))

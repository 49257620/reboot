# encoding: utf-8
# Author: LW

import re

"""
元字符 | 表示或  
"""
print('元字符 | 表示或 ')
print("re.search('liuwei(A|B)', 'liuweiA')", re.search(r'liuwei(A|B)', 'liuweiA'))
print("re.search('liuwei(A|B)', 'liuweiB')", re.search(r'liuwei(A|B)', 'liuweiB'))
print("re.search('liuwei(A|B)', 'liuweiC')", re.search(r'liuwei(A|B)', 'liuweiC'))

print('-' * 50)

"""
脱字符 ^ 表示匹配字符串开始位置  
"""
print('脱字符 ^ 表示匹配字符串开始位置  ')
print("re.search(r'^liuwei','liuwei kaishi')", re.search(r'^liuwei', 'liuwei kaishi'))
print("re.search(r'^liuwei','kaishi liuwei')", re.search(r'^liuwei', 'kaishi liuwei'))

print('-' * 50)

"""
$ 表示匹配字符串结束位置  
"""
print('$ 表示匹配字符串结束位置   ')
print("re.search(r'liuwei$','liuwei kaishi')", re.search(r'liuwei$', 'liuwei kaishi'))
print("re.search(r'liuwei$','kaishi liuwei')", re.search(r'liuwei$', 'kaishi liuwei'))
print('-' * 50)

"""
()\1-99 匹配子组  
"""

print('()\\1-99 匹配子组     ')

print("re.search(r'(abc)\\1','abcdef'')", re.search(r'(abc)\1', 'abcdef'))
print("re.search(r'(abc)\\1','abcabc')", re.search(r'(abc)\1', 'abcabc'))
print("re.search(r'(abc)\\1','abcabcabc')", re.search(r'(abc)\1', 'abcabcabc'))
print('-' * 50)
"""
()\三位数 八进制 匹配asc码  
"""
print('()\\三位数 八进制 匹配asc码   a = 97  八进制为 141  ')

print("re.search(r'(abc)\\141','abca'')", re.search(r'(abc)\141', 'abca'))

print('-' * 50)

"""
元字符 [...] 字符类 
"""
print('元字符 [...] 字符类 \. == [.]  将里面的字符当作普通字符看待，除了几个特殊的字符')

print("re.search(r'.','liuwei')", re.search(r'.', 'liuwei'))
print("re.search(r'\.','abc.com')", re.search(r'\.', 'abc.com'))
print("re.search(r'[.]','abc.com')", re.search(r'[.]', 'abc.com'))

print('- 表示范围')
print("re.findall(r'[a-z]','liuwei.com')", re.findall(r'[a-z]', 'liuwei.com'))

print('\ 放到字符类中会出错,表示转义符  如 \\n')
print("re.findall(r'[\\n]','abc.com\\n')", re.findall(r'[\n]', 'abc.com\n'))

print('^ 表示除外，除了制定字符类中的其他的字符,放在最前面表示取反，放在最后面表示本身')
print("re.findall(r'[a-z]','ABCabc123.com')", re.findall(r'[a-z]', 'ABCabc123.com'))

print('-' * 50)

"""
{M,N} 重复次数
"""
print('{M,N} 重复次数')
print("re.search(r'abc{3}','abccccc')", re.search(r'abc{3}', 'abccccc'))
print("re.search(r'(abc){3}','abcabcabc')", re.search(r'(abc){3}', 'abcabcabc'))
print("re.search(r'(abc){1,5}','abcabcabc')", re.search(r'(abc){1,5}', 'abcabcabc2'))

print('-' * 50)

"""
* 表示 0 到 多次 等于 {0,}
+ 表示 1 到 多次 等于 {1,}
? 表示 0 到 1 次 等于 {0,1}
"""
print('* 表示 0 到 多次 等于 {0,}')
print('+ 表示 1 到 多次 等于 {1,}')
print('? 表示 0 到 1 次 等于 {0,1}')

print('-' * 50)

"""
? 贪婪非贪婪
"""
print('? 贪婪与非贪婪')
s = '<html><title>liuwei</title></html>'
print('s = <html><title>liuwei</title></html>')
print("贪婪:re.search(r'<.+>',s)", re.search(r'<.+>', s))
print("非贪婪:re.search(r'<.+?>',s)", re.search(r'<.+?>', s))

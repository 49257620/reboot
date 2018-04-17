# encoding: utf-8
# Author: LW

import re

"""
\A 匹配字符串开始位置 等于  ^
\Z 匹配字符串结束位置 等于  $
"""
print(' \A 匹配字符串开始位置 等于  ^')
print(' \Z 匹配字符串结束位置 等于  $')


print('-' * 50)
"""
\b 匹配单词边界
"""
print(' \\b 匹配单词边界 ')
print("re.findall(r'\\babc\\b','abc.com')",re.findall(r'\babc\b','abc.com'))
print("re.findall(r'\\babc\\b','(abc).com')",re.findall(r'\babc\b','(abc).com'))
print("re.findall(r'\\babc\\b','abc_com')",re.findall(r'\babc\b','abc_com'))
print("re.findall(r'\\babc\\b','abc efg')",re.findall(r'\babc\b','abc efg'))

print('-' * 50)

"""
\B 匹配非单词边界
"""
print(' \\B 匹配非单词边界 ')
print("re.findall(r'py\\B','python')",re.findall(r'py\B','python'))
print("re.findall(r'py\\B','py.')",re.findall(r'py\B','py.'))


print('-' * 50)

"""
\d 匹配数字  等于  [0-9]
\D 匹配非数字  等于  [^0-9]
\s 匹配空字符  
\S 匹配非空字符
"""
print('\\d 匹配数字  等于  [0-9]')
print('\\D 匹配非数字  等于  [^0-9]')
print('\\s 匹配空字符 ')
print('\\S 匹配非空字符')
print('-' * 50)

"""
\w 匹配单词字符  [a-zA-Z0-9]
\W 与\w 相反
"""
print('\\w 匹配单词字符  [a-zA-Z0-9]')
print('\\W 与\w 相反')
print("re.findall(r'\\w*','你好 abc 123 ABC')",re.findall(r'\w*','你好 abc 123 ABC'))
print("re.findall(r'\\w','你好 abc 123 ABC . _ + !')",re.findall(r'\w','你好 abc 123 ABC . _ + !'))
print("re.findall(r'\\W','你好 abc 12 3ABC . _ + !')",re.findall(r'\W','你好 abc 123 ABC . _ + !'))
print('-' * 50)

"""
编译正则表达式 ，以便频繁使用
"""
print("""
p = re.compile(r'[A-Z]')
print(p.search('ABC abc'))
print(p.findall('ABC abc'))
""")
p = re.compile(r'[A-Z]')
print(p.search('ABC abc'))
print(p.findall('ABC abc'))

print('-' * 50)
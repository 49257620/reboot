# encoding: utf-8
# author = ‘LW’

"""

file read readline readlines 方法
"""

f = open('C:\\PROJECTS\\Python\\tmpfile\\data.txt', 'rt', encoding='utf-8')
"""
print(f .readline())
print(f .readline())
print(f .readline())
print(f .readline())
"""
data = f.readlines()
print(data)
print(f.readlines())
"""
for x in data:
    print(x, end='')
    
"""

data_str = ''.join(data)

print(data_str)

f.close()

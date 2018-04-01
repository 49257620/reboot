# encoding: utf-8
# author = ‘LW’
"""
统计list中每个元素出现的次数
languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp', 'c', 'javascript', 'java', 'python', 'matlab', 'python', 'go', 'java']
提示：
统计结果为element:count的形式，统计结果采用dict
从左到右依次遍历list中元素，判断是否在dict中，如果不在则将element存入dict并设置count为1，否则将dict中element对应的count加1后再存储到dict中


"""

languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp', 'c', 'javascript', 'java', 'python',
             'matlab', 'python', 'go', 'java']

lang_dict = {}

for l in languages:
    if l in lang_dict:
        lang_dict[l] += 1
    else:
        lang_dict[l] = 1

print(lang_dict)

lang_dict_2 = {}
for l in languages:
    lang_dict_2[l] = 1 if l not in lang_dict_2 else lang_dict_2[l] + 1

print(lang_dict_2)

# 通过get +default 设置
lang_dict_3 = {}
for l in languages:
    lang_dict_3[l] = lang_dict_3.get(l, 0) + 1

print(lang_dict_3)
# 通过set +default 设置
lang_dict_4 = {}
for l in languages:
    lang_dict_4[l] = lang_dict_4.setdefault(l, 0) + 1

print(lang_dict_4)

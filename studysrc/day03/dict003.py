# encoding: utf-8
# author = ‘LW’
"""
统计文章中每个英文字母出现的次数
article = 'I was not delivered unto this world in defeat, nor does failure course in my veins. I am not a sheep waiting to be prodded by my shepherd. I am a lion and I refuse to talk, to walk, to sleep with the sheep. I will hear not those who weep and complain, for their disease is contagious. Let them join the sheep. The slaughterhouse of failure is not my destiny.'
提示：判断是否为英文单词
if  (element > ‘a’ and element < ‘z’) or (element > ‘A’ and element < ‘Z’)

"""

article = 'I was not delivered unto this world in defeat, nor does failure course in my veins. I am not a sheep waiting to be prodded by my shepherd. I am a lion and I refuse to talk, to walk, to sleep with the sheep. I will hear not those who weep and complain, for their disease is contagious. Let them join the sheep. The slaughterhouse of failure is not my destiny.'

data_dict = {}

for c in article:
    if c.isalpha():
        if c in data_dict:
            data_dict[c] += 1
        else:
            data_dict[c] = 1

print(data_dict)

data_dict_2 = {}
for c in article:
    if c.isalpha():
        data_dict_2[c.lower()] = 1 if c.lower() not in data_dict_2 else data_dict_2[c.lower()] + 1
    else:
        data_dict_2['其他'] = 1 if '其他' not in data_dict_2 else data_dict_2['其他'] + 1

print(data_dict_2)

data_dict_3 = {}

for c in article:
    if c.isalpha():
        data_dict_3[c] = data_dict_3.setdefault(c, 0) + 1

print(data_dict_3)

data_dict_4 = {}

for c in article:
    if c.isalpha():
        data_dict_4[c] = data_dict_4.get(c, 0) + 1

print(data_dict_4)

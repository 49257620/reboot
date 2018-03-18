# encoding utf-8
promote = float(input('输入分数:'))
rank = 'E'

if promote // 90 >= 1:
    rank = 'A'
elif promote // 80 >= 1:
    rank = 'B'
elif promote // 70 >= 1:
    rank = 'C'
elif promote // 60 >= 1:
    rank = 'D'
else:
    rank = 'E'
print('成绩为：' + rank)



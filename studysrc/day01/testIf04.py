# encoding utf-8
promote = float(input('输入分数:'))
rank = 'E'

if promote >= 90:
    rank = 'A'
elif promote >= 80:
    rank = 'B'
elif promote >= 70:
    rank = 'C'
elif promote >= 60:
    rank = 'D'
else:
    rank = 'E'
print('成绩为：' + rank)

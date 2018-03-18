# encoding utf-8
promote = float(input('输入分数:'))
rank = 'E'

if promote >= 90:
    rank = 'A'
else:
    if promote >= 80:
        rank = 'B'
    else:
        if promote >= 70:
            rank = 'C'
        else:
            if promote >= 60:
                rank = 'D'
            else:
                rank = 'E'
print('成绩为：' + rank)

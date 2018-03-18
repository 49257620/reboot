# encoding utf-8
promote = input('看到西瓜了吗？（看到输入\'Y\'或者\'y\'）:')
money = 100.0
priceBaozi = 11.5
priceXigua = 23.8

print('>>>买了一斤包子，花费'+str(priceBaozi)+'元')
money = money - priceBaozi

if promote == 'Y' or promote == 'y':
    print('>>>买了一个西瓜，花费'+str(priceXigua)+'元')
    money = money - priceXigua

print('剩余：' + str(money) + '元')

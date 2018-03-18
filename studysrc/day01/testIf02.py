# encoding utf-8
promote = input('看到西瓜了吗？（看到输入\'Y\'或者\'y\'）:')
money = 100.0
priceSome = 11.5
priceOne = 1.1

if promote == 'Y' or promote == 'y':
    print('>>>买了一个包子，花费' + str(priceOne) + '元')
    money = money - priceOne
else:
    print('>>>买了一斤包子，花费' + str(priceSome) + '元')
    money = money - priceSome

print('剩余：' + str(money) + '元')

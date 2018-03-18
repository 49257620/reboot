# encoding utf-8
import random

radom_num = random.randint(0, 100)
idx = 1
# print(radom_num)
while True:

    inputInt = int(input("(第" + str(idx) + "/5次)" + "输入数字猜测的数字："))
    if inputInt == radom_num:
        print('猜对了')
        break
    elif inputInt > radom_num:
        print('猜大了')
    else:
        print('猜小了')
    idx += 1
    if idx > 5:
        print('太笨了，下次再来，正确的数字是：' + str(radom_num))
        break

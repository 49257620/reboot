# encoding: utf-8
# Author: LW

import thinkstats
import math


def Pumpkin():
    pump_weight_list = [1, 1, 1, 3, 3, 591]

    mean, var = thinkstats.MeanVar(pump_weight_list)

    print('南瓜的均值为：{0}，方差为：{1}，标准差为：{2}'.format(mean, var, math.sqrt(var)))


if __name__ == '__main__':
    Pumpkin()



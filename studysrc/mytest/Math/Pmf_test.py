# encoding: utf-8
# Author: LW

import Pmf
import matplotlib.pyplot as pyplot

hist = Pmf.MakeHistFromList([1,1,2,2,2,3,4,4,4,4,4,5,5,5,6,6,6,6,6,6,6])

def Mode(hist):
    return sorted(hist.Items(), key=lambda s: s[1], reverse=True)[0][0]

def AllModes(hist):
    return sorted(hist.Items(), key=lambda s: s[1], reverse=True)

print(hist)

print('6在List中出现的频数为：{}'.format(hist.Freq(6)))

print('List中所有的元素去重复为：',hist.Values())
print('List中所有的元素去重复为并排序为：')
print('-'*50)
for item in sorted(hist.Values()):
    print(item)
print('-'*50)
for val, freq in hist.Items():
    print(val, freq)
print('-'*50)
print('按频数降序排列的值—频数对：')
print('-'*50)
reversList = AllModes(hist)
for x,y in reversList:
    print(x,'-', y)
print('-'*50)
print('返回最频繁值：',end='')
max_freq = Mode(hist)
print(max_freq)

"""
vals, freqs = hist.Render()
rectangles = pyplot.bar(vals, freqs)
pyplot.show()

"""
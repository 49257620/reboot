# encoding: utf-8
"""
【程序89】
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
　　　每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
1.程序分析：
2.程序源代码：
"""

code_li = [8, 4, 5, 6]

print('code:', code_li)


def encode(code_li):
    for i in range(len(code_li)):
        code_li[i] = (code_li[i] + 5) % 10

    code_li[0], code_li[3] = code_li[3], code_li[0]
    code_li[1], code_li[2] = code_li[2], code_li[1]

    return code_li


decode_li = encode(code_li)

print('encode:', decode_li)


def decode(decode_li):
    code_li[0], code_li[3] = code_li[3], code_li[0]
    code_li[1], code_li[2] = code_li[2], code_li[1]
    for i in range(len(decode_li)):
        code_li[i] = code_li[i] - 5 if code_li[i] > 5 else code_li[i] + 5

    return code_li


print('decode:', decode(decode_li))

# encoding utf-8


total = 0
avg = 0
idx = 0

while True:
    inputStr = input("输入数字（exit退出）：")
    if inputStr == 'exit':
        break
    total += float(inputStr)
    idx += 1

if idx > 0:
    avg = total / idx
else:
    avg = 0
print('输入次数：', idx, ' 总数：', total, ' 平均数：', avg)

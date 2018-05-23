# encoding: utf-8
# Author: LW

str_input = """2711C03	0046	意外身故，残疾及烧伤(含旅行期间高风险运动保障、酒店意外身故保障、地震意外身故保障、海啸意外身故)|Accidental Death and Disablement & Burns (Include Accidental Death due to hotel-stay, earthquake, tsunami)
2711F28	0041	公共交通工具意外身故、残疾(包含摩托车意外身故保障、长途公共汽车意外身故保障)|Common Carrier Accident (Include Accidental Death due to motorbike-drive, long-distance coach)
2711F33	0047	医疗费用补偿（含意外和急性病）|Medical Expenses - Outpatient (due to accident & acute disease) 
2711F34	0048	住院津贴（含意外和急性病）50元/天（最高30天）|Medical Expenses - Inpatient (due to accident & acute disease) RMB ¥50/per day (most 30 days)
2711F47	0061	突发急性病身故|Death due to Acute Disease
2711F48	0062	自驾车意外身故及残疾|Accidental Death and Disablement due to self-drive
2711F38	0052	旅程延误(300元/每5小时)|Travel Delay(¥300/per 5 hours)
2711F39	0053	行李延误(500元/每8小时)|Baggage Delay(¥500/per 8 hours)
2711F40	0054	旅行取消/变更|Trip Cancellation
2711F06	0007	个人行李（每件或每套行李最高赔偿额为RMB1,000元）|Baggage Loss or Damage(Limit Per Item or Set of Items is RMB1,000)
2711F41	0055	旅行证件重置费用|Loss of Travel document
2711F43	0057	个人责任|Personal Liability
2711F44	0058	银行卡盗刷（不适用未成年人）|Bank Card Fradulent Usage(not applicable to minors)
2711F45	0059	旅行期间家居物品保障（火灾、爆炸、盗窃导致的损失，每件/每套限1000元）|Home Guard Coverage(Limit per item or set of items is RMB1, 000)
2711F30	0043	紧急医疗运送及送返 |Medical evacuation and repatriation
2711F31	0044	遗体或骨灰送返（灵柩费限额6000元，丧葬费用以20,000元为限）|Repatriation or Cremains of Remains （Cremains Expenses Limited to RMB6,000,Funeral Fxpenses Limited to 20000）
2711F32	0045	亲属前往慰问探访|Relative Visit
2711F46	0060	未成年人送返|Return of Minors"""


lines = str_input.split("\n")

kind_item_list = [(x.split('\t')[0], x.split('\t')[1], x.split('\t')[2].replace('|', '\n')) for x in lines]
print(kind_item_list)




"""
for x in kind_item_list:
    print(x[2])
for x in kind_item_list:
    print("('{0}', '{1}', '''{2}'''),".format(x[0], x[1], x[2]).replace('|', '\n'))
aa = [
    ('2711C01', '0001', '''意外身故、残疾及烧伤
Accidental Death and Disablement & Burns'''),
    ('2711F03', '0004', '''紧急医疗运送和送返
Medical evacuation and repatriation'''),
    ('2711F04', '0005', '''身故遗体送返 (其中丧葬费用以16,000元为限)
Repatriation or Cremains of Remains （Funeral Fxpenses Limited to 16000RMB）'''),
    ('2711F18', '0029', '''双倍给付意外伤害（因交通工具）
Double Indemnity'''),
    ('2711F02', '0003', '''旅行紧急医疗费用
Medical Expenses'''),
    ('2711F13', '0014', '''旅行延误 (每5小时延误赔偿额:300元)
Travel Delay(¥300/per 5 hours)'''),
    ('2711F12', '0013', '''行李延误 (每8小时延误赔偿额:人民币500元)
Baggage Delay(¥500/per 8 hours)'''),
    ('2711F21', '0032', '''个人钱财
Loss of personal money'''),
    ('2711F06', '0007', '''旅行者随身财产(每件或每套行李或物品赔偿限额:人民币2,500元)
Baggage Loss or Damage(Limit Per Item or Set of Items is RMB2,500)''')
]
"""
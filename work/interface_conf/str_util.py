# encoding: utf-8
# Author: LW

str_input = """2712C01	001	意外身故、伤残
2712F01	002	猝死
2712F08	009	意外伤害医疗（每次事故免赔额100元）
2712F07	008	急性肠胃炎医疗补偿
2712F22	023	意外伤害住院津贴（30天为限）
2712F09	010	紧急医疗运送及送返
2712F10	011	身故遗体运返（含丧葬费用）"""


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
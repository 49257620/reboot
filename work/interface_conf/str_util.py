# encoding: utf-8
# Author: LW

str_input = """2711C01	0001	意外身故、残疾及烧伤|Accidental Death and Disablement & Burns
2711F03	0004	紧急医疗运送和送返|Medical evacuation and repatriation
2711F04	0005	身故遗体送返 (其中丧葬费用以16,000元为限)|Repatriation or Cremains of Remains （Funeral Fxpenses Limited to 16000RMB）
2711F10	0011	亲属慰问探访补偿|Relative Visit
2711F17	0018	未成年人送返费用补偿|Return of Minors
2711F18	0029	双倍给付意外伤害（因交通工具）|Double Indemnity
2711F02	0003	旅行紧急医疗费用|Medical Expenses
2711F20	0031	旅行绑架及非法拘禁 (每24小时赔偿额:3,000元)|Compassionate Cash due to Kidnaping or illegal detention(3000RMB per 24hours)
2711F13	0014	旅行延误 (每5小时延误赔偿额:300元)|Travel Delay(¥300/per 5 hours)
2711F12	0013	行李延误 (每8小时延误赔偿额:人民币500元)|Baggage Delay(¥500/per 8 hours)
2711F09	0010	旅行变更|Trip Cancellation
2711F07	0008	旅行证件遗失|Loss of Travel document
2711F22	0033	银行卡盗刷|Bank Card Fradulent Usage
2711F21	0032	个人钱财|Loss of personal money
2711F06	0007	旅行者随身财产(每件或每套行李或物品赔偿限额:人民币2,500元)|Baggage Loss or Damage(Limit Per Item or Set of Items is RMB2,500)
2711F11	0012	我们承担旅行期间因意外事故导致他人身体或财务损失而须支付给第三方的赔偿金|Personal Liability"""


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
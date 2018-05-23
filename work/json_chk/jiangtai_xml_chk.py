# encoding: utf-8
# Author: LW


from xml.etree import ElementTree as ET
import time
import math
import dbmanager as hicis

xml_str = """<root>
<policyType>2</policyType>
<policySort>0</policySort>
<agentCode>M00000000008</agentCode>
<operateDate>2018-05-16 19:53:15</operateDate>
<startDate>2018-05-31 00:00:00</startDate>
<endDate>2018-05-31 23:59:59</endDate>
<planCode>P272017JTJJ000604</planCode>
<sumAmount>290000.0</sumAmount>
<sumPremium>1.6</sumPremium>
<classCode>27</classCode>
<riskCode>2712</riskCode>
<businessNature>k</businessNature>
<autoTransRenewFlag>3</autoTransRenewFlag>
<arbitBoardName>北京市仲裁委员会</arbitBoardName>
<sumQuantity>0</sumQuantity>
<proposalAppliInfo><insuredName>山西东方万达进出口贸易有限公司</insuredName>
<identifyType>99</identifyType>
<identifyNumber>91140108097954897Q</identifyNumber>
<postAddress>/</postAddress>
<identifyDate>2023-05-16 00:00:00</identifyDate>
<insuredNature>4</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<birthDate>2018-05-16 19:53:14</birthDate>
<sex></sex>
<phoneNumber>17801089680</phoneNumber>
<mobile>17801089680</mobile>
<email>service@youngmanager.cn</email>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName></linkerName>
<nationalityCode>CHN</nationalityCode>
<invoicetype></invoicetype>
<taxPayerNum></taxPayerNum>
</proposalAppliInfo><proposalInsuredInfoList><insuredName>姚彩霞</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142622198410123725</identifyNumber>
<birthDate>1984-10-12 00:00:00</birthDate>
<age>33</age>
<sex>2</sex>
<identifyDate>2023-05-16 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712C01-001</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712F02-003</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712F04-005</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712F06-007</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712F23-024</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><orderId>201805161822245399499991U7kN</orderId>
<planFeeInfo><serialNo>1</serialNo>
<payNo>1</payNo>
<payReason>R10</payReason>
<planDate>2018-05-16 19:53:15</planDate>
<currency>CNY</currency>
<planFee>1.60</planFee>
<delinquentFee>0.00</delinquentFee>
<planstartdate>2018-05-16 19:53:15</planstartdate>
<productType></productType>
</planFeeInfo><Profit1>0</Profit1>
<Profit1Value></Profit1Value>
<Profit2>0</Profit2>
<Profit2Value></Profit2Value>
<travelInfo><destinationCountry>KOR</destinationCountry>
<destinationArea></destinationArea>
<travelNO></travelNO>
<leaveTime>2018-07-16 19:53:15</leaveTime>
<guideName></guideName>
<guidePhone></guidePhone>
<guideEmail></guideEmail>
<trafficNumber>---</trafficNumber>
</travelInfo><requestInfo><user>jiangtai</user>
<password>zYjv9SSB</password>
<transcationCode>201805161822245399499991U7kN213</transcationCode>
</requestInfo><productCode></productCode>
</root>
"""

root =ET.XML(xml_str)

start_time = time.strptime(root.find('startDate').text, '%Y-%m-%d %H:%M:%S')
end_time = time.strptime(root.find('endDate').text, '%Y-%m-%d %H:%M:%S')
risk_code = root.find('riskCode').text
plan_code = root.find('planCode').text
product_code = plan_code[:-2]
order_id = root.find('orderId').text
agent_code = root.find('agentCode').text
sum_amount = float(root.find('sumAmount').text)
sum_premium = float(root.find('sumPremium').text)
apply_info_root = root.find('proposalAppliInfo')
insured_list = root.findall('proposalInsuredInfoList')
insured_cnt = len(insured_list)


chk_product_code = ''
chk_product_name = ''
chk_plan_code = ''
chk_plan_name = ''
chk_plan_sum_amount = 0.0

days = math.floor((time.mktime(end_time) - time.mktime(start_time)) / (60 * 60 * 24)) + 1

print("开始检查xml报文内容:")

sql = """select b.PRODUCTCODE,b.PRODUCTNAME,a.PROGRAMMECODE,a.PROGRAMMENAME,a.SUMAMOUNT 
from PRPDPROGRAMME a,PRPDPRODUCT b 
where a.PROGRAMMECODE='{0}'
and a.PRODUCTCODE = b.PRODUCTCODE""".format(plan_code)

row = hicis.find_one(sql)

if row:
    chk_product_code = row[0]
    chk_product_name = row[1]
    chk_plan_code = row[2]
    chk_plan_name = row[3]
    chk_plan_sum_amount = row[4]
    print("1.方案代码：输入：", plan_code)
    print('\tV 产品代码：', chk_product_code, '\n\tV 产品名称：', chk_product_name, '\n\tV 方案代码：', chk_plan_code, '\n\tV 方案名称：',
          chk_plan_name,
          '\n\tV 单人保额：', chk_plan_sum_amount)

    print("2.保额检查：输入：", sum_amount)

    if sum_amount == chk_plan_sum_amount * insured_cnt:
        print('\tV 检查结果：', '符合', chk_plan_sum_amount, '*', insured_cnt,
              '=', sum_amount)
    else:
        print('\tX 检查结果：', '不符合', chk_plan_sum_amount, '*', insured_cnt,
              '=', chk_plan_sum_amount * insured_cnt)

    print("3.保费检查：输入：", sum_premium)
    chk_sum_premium = 0.0
    insured_idx = 1
    for insured in insured_list:
        sql = """select SUM(PREMIUM) from prpdratedate
where PLANCODE='{0}'
and TERMMINVALUE <= {1} AND TERMMAXVALUE >={1}
and AGEMINVALUE <= {2} AND AGEMAXVALUE>={2}
        """.format(plan_code,  days,int(insured.find('age').text))
        row = hicis.find_one(sql)
        chk_sum_premium += row[0]
        print('\t\t {3:3d} 姓名：{0:5s} 年龄：{1:^3d} 保费：{2}  天数:{4}'.format(insured.find('insuredName').text, int(insured.find('age').text),row[0],insured_idx,days))
        insured_idx +=1
    if round(chk_sum_premium,2) == sum_premium :
        print('\tV 检查结果：', '符合', sum_premium)
    else:
        print('\tX 检查结果：', '不符合','合计人数：',insured_cnt, ' 输入：',sum_premium,'方案：',round(chk_sum_premium,2))


else:
    print("方案不存在")


# sql = 'SELECT * FROM prpcmain where rownum<10'
# row = hicis.find_one(sql)

# print(row)

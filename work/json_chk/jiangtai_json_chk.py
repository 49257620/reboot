# encoding: utf-8
# Author: LW


import json
import time
import math
import dbmanager as hicis

json_str = '{"agentCode":"M00000000008","arbitBoardName":"北京市仲裁委员会","autoTransRenewFlag":"3","businessNature":"k","classCode":"27","endDate":"2018-05-31T23:59:59","operateDate":"2018-05-16T19:53:15","orderId":"201805161822245399499991U7kN","planCode":"P272017JTJJ000604","planFeeInfo":{"currency":"CNY","delinquentFee":"0.00","payNo":"1","payReason":"R10","planDate":"2018-05-16T19:53:15","planFee":"1.60","planstartdate":"2018-05-16T19:53:15","serialNo":1,"__hashCodeCalc":false},"policySort":"0","policyType":"2","proposalAppliInfo":{"account":"","bank":"","email":"service@youngmanager.cn","identifyDate":"2023-05-16","identifyNumber":"91140108097954897Q","identifyType":"99","insuredAddress":"/","insuredIdentity":"99","insuredName":"山西东方万达进出口贸易有限公司","insuredNature":"4","mobile":"17801089680","nationalityCode":"CHN","phoneNumber":"17801089680","postAddress":"/","postCode":"110100","__hashCodeCalc":false},"proposalInsuredInfoList":[{"account":"","age":33,"bank":"","benefitFlag":"","benefitRate":0.0,"birthDate":"1984-10-12","email":"","identifyDate":"2023-05-16","identifyNumber":"142622198410123725","identifyType":"01","insuredAddress":"/","insuredFlag":"1","insuredIdentity":"99","insuredName":"姚彩霞","insuredNature":"3","linkerName":" ","mobile":"","nationalityCode":"CHN","occupationCode":"*","phoneNumber":"13800000000","postAddress":"","postCode":"110100","relateSerialNo":557,"serialNo":"1","sex":"2","__hashCodeCalc":false}],"requestInfo":{"password":"zYjv9SSB","transcationCode":"201805161822245399499991U7kN213","user":"jiangtai","__hashCodeCalc":false},"riskCode":"2712","riskInfoList":[{"amount":0.0,"compensateFlag":"","kindCode":"","netPremium":0.0,"premium":0.0,"standPremium":0.0,"taxFee":0.0,"taxRate":0.0,"__hashCodeCalc":false}],"startDate":"2018-05-31T00:00:00","sumAmount":290000.0,"sumPremium":1.6,"sumQuantity":0,"travelInfo":{"destinationArea":"","destinationCountry":"KOR","guideEmail":"","guideName":"","guidePhone":"","leaveTime":"2018-07-16T19:53:15","trafficNumber":"---","travelNO":"","__hashCodeCalc":false},"__hashCodeCalc":false}'

ll = json.loads(json_str)

start_time = time.strptime(ll['startDate'], '%Y-%m-%dT%H:%M:%S')
end_time = time.strptime(ll['endDate'], '%Y-%m-%dT%H:%M:%S')
risk_code = ll['riskCode']
plan_code = ll['planCode']
product_code = plan_code[:-2]
order_id = ll['orderId']
agent_code = ll['agentCode']
sum_amount = float(ll['sumAmount'])
sum_premium = float(ll['sumPremium'])
apply_info = ll['proposalAppliInfo']
insured_list = ll['proposalInsuredInfoList']
insured_cnt = len(insured_list)

chk_product_code = ''
chk_product_name = ''
chk_plan_code = ''
chk_plan_name = ''
chk_plan_sum_amount = 0.0

days = math.floor((time.mktime(end_time) - time.mktime(start_time)) / (60 * 60 * 24)) + 1

print("开始检查json报文内容:")

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

    print("3.保费检查：输入：", sum_premium,' 天数：',days)
    chk_sum_premium = 0.0
    insured_idx = 1
    for insured in insured_list:
        sql = """select SUM(PREMIUM) from prpdratedate
where PLANCODE='{0}'
and TERMMINVALUE <= {1} AND TERMMAXVALUE >={1}
and AGEMINVALUE <= {2} AND AGEMAXVALUE>={2}
        """.format(plan_code,  days,insured['age'])
        row = hicis.find_one(sql)
        chk_sum_premium += row[0]
        print('\t\t {3:3d} 姓名：{0:5s} 年龄：{1:^3d} 保费：{2} 天数：{4}'.format(insured['insuredName'], insured['age'],row[0],insured_idx,days))
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

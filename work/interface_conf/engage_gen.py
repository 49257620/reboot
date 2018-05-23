# encoding: utf-8
# Author: LW

"""
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2711',1,'T0P272018JTJJ000301','',0,0);

"""
SQL_TMPL = "INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('{0}',{1},'T0{2}','{3}',{4},{5});"
LEN_LIMIT = 35

CHANGE_ID = 'CR2018000042'
RISK_CODE = '2712'
PLAN_CODE = 'P272017JTJJ000604'
CLAUSE_TEXT = """1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
2.本产品承保年龄为30天（含）-85周岁（含）。
3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。
4.同一投保人为同一被保险人投保，仅限在其同一旅行期间内投保本产品其中一款一份，不得投保多份；若投保多款产品或投保同一款产品多份的，被保险人仅能享受其中保障最高的一款产品的一份保险保障。
5.本产品承保中国大陆地区（不包含香港、澳门及台湾）发生的意外伤害事故。
6.在中国境内（不含港澳台）的外籍人士购买本产品需满足：在中国境内工作或居住满183天以上；如涉及紧急救援，将送返至被保险人在中国的常住地址。
7.本保险产品中高风险运动均按照《附加高风险运动意外伤害保险条款》中对高风险运动的释义约定执行，攀岩、快艇、需要佩戴防护器械的拓展训练、需要戴水肺的潜水、蹦极跳属于高风险活动范围。观赏马戏表演及近距离接触动物、休闲性质的滑雪、不需要戴水肺的潜水、漂流、竹筏、骑马、自行车运动、邮轮不属于高风险运动范围，若因参加上述项目发生意外伤害事故，属于意外伤害保险责任范围。
8.合理医疗费用指符合投保所在地及符合条款要求的医院的基本医疗保险规定的药品目录、诊疗项目目录、服务设施范围和支付标准的医疗费用, 不包括基本医疗保险规定的由个人先行自付部分的医疗费用以及基本医疗保险规定之外的应当由个人全额负担的自费费用。请注意:北京市平谷区所有医院的就医均不给予理赔。
9.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。
10.本产品支持当天投保生效，投保支付成功1小时后生效。除航班延误保险责任外，该保单其他保险产品的保险责任起期以保险单载明的保险期间的开始时间为准，航班延误保险责任的保险责任起期为保险单载明的保险期间的开始时间的次日零时。
11.境内旅行医疗费用保险金包含意外伤害及急性病医疗保险金（合理医疗费用：100元免赔额；100%给付），被保险人不论发生高风险运动医疗还是其他意外医疗及急性病医疗，累计给付金额以境内旅行医疗费用保险金额为限。
12.因公共交通工具意外伤害事故导致身故或伤残的，除获得“意外伤害保险金”的给付外，还可同时获得“公共交通工具意外伤害保险金”的给付。
13.急性病身故保险金含猝死保险金。
14.保单查询及报案客服热线400-616-1188。"""

deal_txt = CLAUSE_TEXT
seq_no = 2;

out_file = open('./sql_script/' + PLAN_CODE + '_PRPDENGAGE.sql', 'wt', encoding='utf-8')
out_file.write("/*\n" + CLAUSE_TEXT + "\n*/\n\n\n")
out_file.write("DELETE FROM PRPDENGAGE WHERE CLAUSECODE = 'T0" + PLAN_CODE + "';\n")
out_file.write("INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('"+RISK_CODE+"',1,'T0" + PLAN_CODE + "','特别约定：',0,0);\n")
while True:
    tmp = deal_txt[0:LEN_LIMIT]
    out_file.write(
        SQL_TMPL.format(RISK_CODE, seq_no, PLAN_CODE, tmp, 1 if seq_no == 1 else 1, 1 if seq_no == 1 else 1) + "\n")
    deal_txt = deal_txt[LEN_LIMIT:]
    if len(deal_txt) == 0:
        break
    seq_no += 1

out_file.close()

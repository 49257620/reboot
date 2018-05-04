# encoding: utf-8
# Author: LW

"""
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2711',1,'T0P272018JTJJ000301','',0,0);

"""
SQL_TMPL = "INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('{0}',{1},'T0{2}','{3}',{4},{5});"
LEN_LIMIT = 35

RISK_CODE = '2975'
PLAN_CODE = 'P292018JTJJ001202'
CLAUSE_TEXT = """特别约定：
1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
2.本计划的承保年龄为16至65周岁,以保单生效时的周岁年龄为准。60周岁以上的被保险人,其涉及“意外身故、残疾保障”、“急性病身故保障”、“医疗费用保障”保险金额为上表所载金额的一半,保险费维持不变。
3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。
4.因坠落导致的意外伤害身故、伤残时，坠落意外伤害身故、伤残保险金与意外伤害身故、伤残保险金累计赔付（因坠落导致的意外伤害身故、伤残时，户外人身意外伤害保险金为150000元；一般意外伤害导致身故、伤残时，户外人身意外伤害保险金为100000元）。
5.全球保险方案承保区域为全球（包括中国境内、且含香港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游目的地国家和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告为紧急状态的国家和地区。
6.本计划可承保游客在合法经营场地内进行的滑翔翼、滑翔伞、跳伞、高空弹跳、热气球等空中运动。
7.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求。
8.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。
9.如发生理赔，需提供当天飞行记录的视频或照片用于确认保险事故的相关情况。
10.本产品限购3份，叠加保额仅限死亡伤残保险责任和医疗费用。
11.江泰客服电话：400-616-1188"""

deal_txt = CLAUSE_TEXT
seq_no = 1;

out_file = open('./sql_script/' + PLAN_CODE + '_PRPDENGAGE.sql', 'wt', encoding='utf-8')
out_file.write("/*\n" + CLAUSE_TEXT + "\n*/\n\n\n")
out_file.write("DELETE FROM PRPDENGAGE WHERE CLAUSECODE = 'T0" + PLAN_CODE + "';\n")
while True:
    tmp = deal_txt[0:LEN_LIMIT]
    out_file.write(
        SQL_TMPL.format(RISK_CODE, seq_no, PLAN_CODE, tmp, 0 if seq_no == 1 else 1, 0 if seq_no == 1 else 1) + "\n")
    deal_txt = deal_txt[LEN_LIMIT:]
    if len(deal_txt) == 0:
        break
    seq_no += 1

out_file.close()

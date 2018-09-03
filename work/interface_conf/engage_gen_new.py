# encoding: utf-8
# Author: LW
import os
"""
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2711',1,'T0P272018JTJJ000301','',0,0);

"""
SQL_TMPL = "INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('{0}',{1},'T0{2}','{3}',{4},{5});"
LEN_LIMIT = 35

CHANGE_ID = 'CR2018000074'
RISK_CODE = '2975'
PLAN_CODE = 'P292018MCJJ000701'
CLAUSE_TEXT = """1、本计划仅承保被保险人在中国大陆境内正规游泳馆进行游泳培训期间发生的意外伤害事故，保险人仅承保10次游泳培训课程，培训期间必须有专业教练监护。
2、本产品承保年龄为5-18周岁(含5、18周岁)。
3、在同一保险期间内，每位被保险人仅限投保一份旅行意外伤害保险。若同一个被保险人就同一旅行同时投保2份（或以上）任何旅游险产品，则仅按保额最高者作出赔偿。
4、被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从领队、教练或现场安全人员的要求及劝阻。
5、意外医疗保险根据当地社会医疗保险主管部门规定可报销范围内扣除人民币100元免赔额后，按100%的比例给付医疗保险金；
6、被保险人就诊医院为本市行政区各镇级或以上医院,外地出险可在当地县(区)级及以上医院就医,需转送其他外地医院的,须由当地医疗出具转院证明,并事先征得本公司同意,否则本公司有权不负赔偿责任,如在紧急情况下,允许到镇级以上医院救治,但本公司仅负责事故当天的医疗费用,且以用药日清单为准；
7、被保险人发生保险事故后必须在48小时内向我司报案；报案超一个月，不予受理。提出索赔时,必须提供医疗费用的原件,且被保险人报案后72小时内保险人保留对伤者验伤的权利,如无法见到伤者,保险人有权拒赔.
8、被保险人在学习期间必须要持有游泳教练证的教练员在场指导及保护。"""

deal_txt = CLAUSE_TEXT
seq_no = 2;
if not os.path.exists('./sql_script_ch' + os.sep + CHANGE_ID):
    os.mkdir('./sql_script_ch' + os.sep + CHANGE_ID)
out_file = open('./sql_script_ch' + os.sep + CHANGE_ID + os.sep + PLAN_CODE + '_PRPDENGAGE.sql', 'wt', encoding='utf-8')
out_file.write("/*\n" + CLAUSE_TEXT + "\n*/\n\n\n")
out_file.write("DELETE FROM PRPDENGAGE WHERE CLAUSECODE = 'T0" + PLAN_CODE + "';\n")
out_file.write("INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('"+RISK_CODE+"',1,'T0" + PLAN_CODE + "','特别约定：\n',0,0);\n")
while True:
    tmp = deal_txt[0:LEN_LIMIT]
    out_file.write(
        SQL_TMPL.format(RISK_CODE, seq_no, PLAN_CODE, tmp, 1 if seq_no == 1 else 1, 1 if seq_no == 1 else 1) + "\n")
    deal_txt = deal_txt[LEN_LIMIT:]
    if len(deal_txt) == 0:
        break
    seq_no += 1

out_file.close()

# encoding: utf-8
# Author: LW
import os
"""
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2711',1,'T0P272018JTJJ000301','',0,0);

"""
SQL_TMPL = "INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('{0}',{1},'T0{2}','{3}',{4},{5});"
LEN_LIMIT = 35

CHANGE_ID = 'CR2018000032'
RISK_CODE = '2712'
PLAN_CODE = 'P272018JTJJ000201'
CLAUSE_TEXT = """1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
2.本产品承保年龄为出生满30天（含）---85周岁。（含）
3.本产品承保中国大陆地区（不包含香港、澳门及台湾）发生的意外伤害事故。
4.同一投保人为同一被保险人投保，仅限在其同一旅行期间内投保一日游保险产品一份，不得投保多份；若投保多份的，被保险人仅能享受其中一份保险保障。
5.本产品支持当日投保、当日起保，最早生效时间为支付成功及时生效，保险止期截止到当日24时。
6.保险责任的开始时间以下列情况中最迟发生的时间为准：
(1)保险单所载的保险期间起始日；
(2)被保险人在保险期间内离开其中国境内日常居住地或日常工作地前往旅行目的地。
保险责任的终止时间以下列情况中最先发生的时间为准：
(1)保险单或保险凭证所载保险期间届满；
(2)该被保险人完成旅行后返回至其中国境内日常居住地或日常工作地。
7.若因公共交通工具意外伤害事故导致身故或伤残的，除获得“意外伤害保险金”的给付外，还可同时获得“公共交通工具意外伤害保险金”的给付。
8.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。
9.本保险中的境内旅行医疗费用保险金包含急性病医疗费用保险金。"""

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

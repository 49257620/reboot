# encoding: utf-8
# Author: LW

from product_gen_new_conf import ENGAGE_SQL_TMPL,EPOLICY_TMPL,PLAN_CHK_TMPL,PRODUCT_TMPL,PRODUCT_RISK_TMPL,PLAN_TMPL,PLAN_DCODE_TMPL,CLAUSE_KIDN_TMPL,EPOLICY_KIND_ITEM_TMPL
import os

COMMON_ENGAGE = '''1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
2.本计划的承保年龄为1至85周岁,以保单生效时的周岁年龄为准。71至85周岁的被保险人,其涉及“意外身故、残疾保障”、“公共交通工具意外保障”、“急性病身故保障”、“自驾车意外身故、残疾“保险金额为上表所载金额的一半,保险费维持不变。
3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。
4.在同一保险期间，每位被保险人投保同一产品（包括同一产品的同一计划或不同计划）限投保一份，如果投保了多份同一计划，以最先投保之保单为有效，其余部分视为无效，保险费将无息退还；如果投保了多份不同计划，以意外伤害保额最高之保单为有效，其余部分视为无效，保险费将无息退还。
5.若被保险人在任意渠道投保由本公司承保的多份“意外身故、残疾保险”、“疾病身故”、“急性病身故”、“猝死”、 “意外医疗费用”、“医疗费用(包含意外及突发急性病医疗费用)”、“意外每日住院津贴”、“每日住院津贴”,则本公司仅按其中保险金额最高者做出赔偿。
6.如投保全年保障,每次旅行的最长承保时间为30天。
7.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求。
8.本保险仅承保在中华人民共和国大陆地区境内（不含香港、澳门、台湾）地区。
9.本产品指定医院为符合条款要求的医院,除了北京平谷区所有医院。请注意:北京市平谷区所有医院的就医均不给予理赔。
10. 被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。
11.本产品可承保本市旅游，理赔时需提供相关证明，包括但不限于景点门票、过路费票据、公共交通票据等。'''

LEN_LIMIT = 35
BDDJ_YN = False
CHANGE_ID = 'CR2018000095'
GEN_DATE = '20-08-2018'
AGENT_CODE = 'M00000000063'
AGENT_AGREEN = 'M00000000063-01'
RISK_CODE = '2712'
RISK_NAME = '境内旅行意外伤害保险'
PRODCUT_CODE = 'P272018SJKY0001'
PRODCUT_NAME = '境内旅游意外险'
PLAN_LIST = [
    [
        'P272018SJKY000101',
        '计划一',
        241200.00,
        [('2712C01', '001', '意外身故、伤残'), ('2712F01', '002', '猝死'), ('2712F08', '009', '意外伤害医疗（每次事故免赔额100元）'),
         ('2712F07', '008', '急性肠胃炎医疗补偿'), ('2712F22', '023', '意外伤害住院津贴（30天为限）'), ('2712F09', '010', '紧急医疗运送及送返'),
         ('2712F10', '011', '身故遗体运返（含丧葬费用）')]
        ,
        COMMON_ENGAGE
    ],
    [
        'P272018SJKY000102',
        '计划二',
        352000.00,
        [('2712C01', '001', '意外身故、伤残'), ('2712F01', '002', '猝死'), ('2712F08', '009', '意外伤害医疗（每次事故免赔额100元）'),
         ('2712F07', '008', '急性肠胃炎医疗补偿'), ('2712F22', '023', '意外伤害住院津贴（30天为限）'), ('2712F09', '010', '紧急医疗运送及送返'),
         ('2712F10', '011', '身故遗体运返（含丧葬费用）')]
        ,
        COMMON_ENGAGE
    ],
    [
        'P272018SJKY000103',
        '计划三',
        512100.00,
        [('2712C01', '001', '意外身故、伤残'), ('2712F01', '002', '猝死'), ('2712F08', '009', '意外伤害医疗（每次事故免赔额100元）'),
         ('2712F07', '008', '急性肠胃炎医疗补偿'), ('2712F22', '023', '意外伤害住院津贴（30天为限）'), ('2712F09', '010', '紧急医疗运送及送返'),
         ('2712F10', '011', '身故遗体运返（含丧葬费用）')]
        ,
        COMMON_ENGAGE
    ]
]

if not os.path.exists('./sql_script_ch' + os.sep + CHANGE_ID):
    os.mkdir('./sql_script_ch' + os.sep + CHANGE_ID)


seq_no = 1;

out_file = open('./sql_script_ch' + os.sep + CHANGE_ID + os.sep  + RISK_CODE + "_" + PRODCUT_CODE + "_" + PRODCUT_NAME + '_PRODUCT.sql', 'wt',
                encoding='utf-8')
out_file.write("SET DEFINE OFF;\n")
out_file.write("/****\n")

out_file.write("""
GEN_DATE = '{0}'
AGENT_CODE = '{1}'
AGENT_AGREEN = '{2}'
RISK_CODE = '{3}'
RISK_NAME = '{4}'
PRODCUT_CODE = '{5}'
PRODCUT_NAME = '{6}'
PLAN_LIST = {7}
""".format(GEN_DATE, AGENT_CODE, AGENT_AGREEN, RISK_CODE, RISK_NAME, PRODCUT_CODE, PRODCUT_NAME, PLAN_LIST))

out_file.write("*/\n")
out_file.write("-- 产品信息\n")
procduct_sql = PRODUCT_TMPL.format(PRODCUT_CODE, PRODCUT_NAME, AGENT_CODE, GEN_DATE)
procduct_sql += PRODUCT_RISK_TMPL.format(PRODCUT_CODE, RISK_CODE, RISK_NAME, GEN_DATE)

out_file.write(procduct_sql)

out_file.write("\n\n")

out_file.write("-- 方案信息  \n")

for plan in PLAN_LIST:
    out_file.write("\n-- 方案信息 - " + plan[1] + "\n")
    plan_sql =PLAN_TMPL.format(PRODCUT_CODE, plan[0], plan[1], plan[2], GEN_DATE)
    plan_sql += PLAN_DCODE_TMPL.format(plan[0], plan[1], AGENT_AGREEN)
    out_file.write(plan_sql)

    out_file.write("\n-- 方案信息 - 保障责任关联\n")
    for x in plan[3]:
        clause_kind_sql = CLAUSE_KIDN_TMPL.format(RISK_CODE, plan[0], x[0], x[1])
        out_file.write(clause_kind_sql)
    out_file.write("\n-- 电子保单保险责任显示\n")
    for x in plan[3]:
        epolicy_kind_item_sql = EPOLICY_KIND_ITEM_TMPL.format(plan[0], x[0], x[1], x[2])
        out_file.write(epolicy_kind_item_sql)

    out_file.write("\n\n")

    out_file.write("-- 方案信息 - 特别约定\n")
    out_file.write("/*\n" + plan[4] + "\n*/\n\n\n")
    out_file.write("DELETE FROM PRPDENGAGE WHERE CLAUSECODE = 'T0" + plan[0] + "';\n")
    out_file.write(
        "INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('" + RISK_CODE + "',1,'T0" + plan[0] + "','特别约定：\n',0,0);\n")
    chk_out_file = open('./sql_script_ch' + os.sep + CHANGE_ID + os.sep + RISK_CODE + "_" + plan[0] + "_" + plan[1] + '_INFCHK.sql', 'wt',
                        encoding='utf-8')

    chk_out_file.write(PLAN_CHK_TMPL.format(plan[0], AGENT_CODE, RISK_CODE))

    chk_out_file.close()

    deal_txt = plan[4]
    seq_no = 2
    while True:
        tmp = deal_txt[0:LEN_LIMIT]
        out_file.write(
            ENGAGE_SQL_TMPL.format(RISK_CODE, seq_no, plan[0], tmp, 1 if seq_no == 1 else 1,
                                   1 if seq_no == 1 else 1) + "\n")
        deal_txt = deal_txt[LEN_LIMIT:]
        if len(deal_txt) == 0:
            break
        seq_no += 1
    out_file.write("\n\n")

    """
    eploicy_out_file = open('./sql_script_ch' + os.sep + CHANGE_ID + os.sep + RISK_CODE + "_" + plan[0] + "_" + plan[1] + '_EPOLICY.sql',
                            'wt',
                            encoding='utf-8')

    eploicy_out_file.write(EPOLICY_TMPL.format(plan[0], RISK_NAME))
    eploicy_out_file.close()
    """

out_file.close()



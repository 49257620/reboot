# encoding: utf-8
# Author: LW

from product_gen_new_conf import ENGAGE_SQL_TMPL,EPOLICY_TMPL,PLAN_CHK_TMPL,PRODUCT_TMPL,PRODUCT_RISK_TMPL,PLAN_TMPL,PLAN_DCODE_TMPL,CLAUSE_KIDN_TMPL,EPOLICY_KIND_ITEM_TMPL
import os

COMMON_ENGAGE = '''1.所有的保险责任及条款均以现代财产保险（中国）有限公司签发的正式保险合同之相应条款为准。
2.本计划的承保年龄为1至85周岁,以保单生效时的周岁年龄为准。65至85周岁的被保险人,其涉及“意外身故、残疾保障”、“公共交通工具意外保障”、“急性病身故保障”、“自驾车意外身故、残疾“保险金额为上表所载金额的一半,保险费维持不变。
3.在同一保险期间，每位被保险人投保同一产品（包括同一产品的同一计划或不同计划）限投保一份，如果投保了多份同一计划，以最先投保之保单为有效，其余部分视为无效，保险费将无息退还；如果投保了多份不同计划，以意外伤害保额最高之保单为有效，其余部分视为无效，保险费将无息退还。
4.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。
5.本保险计划承保下列高风险运动项目:海拔6000米以下的休闲旅游、远足徒步、登山运动、山地穿越、露营、固定路线洞穴体验、野外生存;定向运动、拓展活动、场地趣味活动、骑马、马术;自行车运动、山地自行车越野、场地/越野轮滑、自驾车旅行;游泳、潜水(下潜深度不超过18米)、溯溪、划船、帆船、帆板、皮划艇、漂流；;丛林飞跃、飞盘、海上摩托、速降、越野跑(不超过60公里）。
6.本保险计划不承保下列高风险运动项目:海拔6000米以上的攀登、高山滑翔、极地探险,非固定路线洞穴探险、蹦极、自由式潜水(下潜深度超过18米,无水下呼吸设备)、赛车、跳伞、滑翔翼等高风险探险类活动。不承保被保险人违规进入国家或当地政府明令禁止的线路的考察、户外及旅游活动及任何无人区进行的探险、考察。探险指明知在某种特定的自然条件下有失去生命或使身体受到伤害的危险，而故意使自己置身于其中的行为，如：江河漂流、技术性登山、徒步穿越沙漠或人迹罕至的原始森林等活动。
7.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求,但不承保回原国籍。
8.本产品仅承保中国大陆地区（不包含香港、澳门及台湾）发生的意外伤害事故。
9.如保险期间为一年,每次承保最长期限为30天。
10.本产品指定医院为符合条款要求的医院,除了北京平谷区所有医院。请注意:北京市平谷区所有医院的就医均不给予理赔。
11.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。
12.若同一个被保险人为同一旅行或户外运动自愿投保由本保险公司所承保的多份综合保险，且在不同保障产品中有相同保险利益的，则本保险公司仅按其中保险金额最高者做出赔偿，并退还其它保险项下已收取的相应保险利益的保险费。'''

LEN_LIMIT = 35
BDDJ_YN = False
CHANGE_ID = 'CR2018000048'
GEN_DATE = '13-06-2018'
AGENT_CODE = 'M00000000059'
AGENT_AGREEN = 'M00000000059-01'
RISK_CODE = '2975'
RISK_NAME = '户外人身意外伤害保险'
PRODCUT_CODE = 'P292018JUNT0009'
PRODCUT_NAME = '户外安心户外运动保障'
PLAN_LIST = [
    [
        'P292018JUNT000901',
        '计划一',
        170000.00,
        [('2975C01', '001', '意外身故、残疾'), ('2975F17', '018', '公共交通工具意外身故、残疾'),
         ('2975F01', '002', '意外医疗（每次事故免赔为扣除200元后按90%赔付）'), ('2975F06', '007', '紧急医疗运送及送返'), ('2975F10', '011', '个人责任')]
        ,
        COMMON_ENGAGE
    ],
    [
        'P292018JUNT000902',
        '计划二',
        337500.00,
        [('2975C01', '001', '意外身故、残疾'), ('2975F17', '018', '公共交通工具意外身故、残疾'),
         ('2975F01', '002', '意外医疗（每次事故免赔为扣除200元后按90%赔付）'), ('2975F06', '007', '紧急医疗运送及送返'),
         ('2975F07', '008', '身故遗体送返（含丧葬费用）'), ('2975F02', '003', '意外每日住院津贴（30天为限）'), ('2975F10', '011', '个人责任')]
        ,
        COMMON_ENGAGE
    ],
    [
        'P292018JUNT000903',
        '计划三',
        511500.00,
        [('2975C01', '001', '意外身故、残疾'), ('2975F17', '018', '公共交通工具意外身故、残疾'),
         ('2975F01', '002', '意外医疗（每次事故免赔为扣除200元后按90%赔付）'), ('2975F06', '007', '紧急医疗运送及送返'),
         ('2975F07', '008', '身故遗体送返（含丧葬费用）'), ('2975F02', '003', '意外每日住院津贴（30天为限）'), ('2975F10', '011', '个人责任')]
        ,
        COMMON_ENGAGE
    ],
    [
        'P292018JUNT000904',
        '计划四',
        758000.00,
        [('2975C01', '001', '意外身故、残疾'), ('2975F17', '018', '公共交通工具意外身故、残疾'),
         ('2975F01', '002', '意外医疗（每次事故免赔为扣除200元后按90%赔付）'), ('2975F06', '007', '紧急医疗运送及送返'),
         ('2975F07', '008', '身故遗体送返（含丧葬费用）'), ('2975F02', '003', '意外每日住院津贴（30天为限）'), ('2975F10', '011', '个人责任')]
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



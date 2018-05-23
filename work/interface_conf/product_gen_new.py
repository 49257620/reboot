# encoding: utf-8
# Author: LW

from product_gen_new_conf import ENGAGE_SQL_TMPL,EPOLICY_TMPL,PLAN_CHK_TMPL,PRODUCT_TMPL,PRODUCT_RISK_TMPL,PLAN_TMPL,PLAN_DCODE_TMPL,CLAUSE_KIDN_TMPL,EPOLICY_KIND_ITEM_TMPL

LEN_LIMIT = 35
BDDJ_YN = False

GEN_DATE = '14-05-2018'
AGENT_CODE = 'M00000000054'
AGENT_AGREEN = 'M00000000054-02'
RISK_CODE = '2711'
RISK_NAME = '境外旅行保险'
PRODCUT_CODE = 'P272018BCJJ0006'
PRODCUT_NAME = '蚝友行-境外旅行险-东南亚'
PLAN_LIST = [
    [
        'P272018BCJJ000601',
        '基础版',
        1234300.00,
        [('2711C03', '0046',
          '意外身故，残疾及烧伤(含旅行期间高风险运动保障、酒店意外身故保障、地震意外身故保障、海啸意外身故)\nAccidental Death and Disablement & Burns (Include Accidental Death due to hotel-stay, earthquake, tsunami)'),
         ('2711F28', '0041',
          '公共交通工具意外身故、残疾(包含摩托车意外身故保障、长途公共汽车意外身故保障)\nCommon Carrier Accident (Include Accidental Death due to motorbike-drive, long-distance coach)'),
         ('2711F33', '0047', '医疗费用补偿（含意外和急性病）\nMedical Expenses - Outpatient (due to accident & acute disease) '), (
         '2711F34', '0048',
         '住院津贴（含意外和急性病）50元/天（最高30天）\nMedical Expenses - Inpatient (due to accident & acute disease) RMB ¥50/per day (most 30 days)'),
         ('2711F47', '0061', '突发急性病身故\nDeath due to Acute Disease'),
         ('2711F48', '0062', '自驾车意外身故及残疾\nAccidental Death and Disablement due to self-drive'),
         ('2711F38', '0052', '旅程延误(300元/每5小时)\nTravel Delay(¥300/per 5 hours)'),
         ('2711F39', '0053', '行李延误(500元/每8小时)\nBaggage Delay(¥500/per 8 hours)'),
         ('2711F40', '0054', '旅行取消/变更\nTrip Cancellation'), ('2711F06', '0007',
                                                             '个人行李（每件或每套行李最高赔偿额为RMB1,000元）\nBaggage Loss or Damage(Limit Per Item or Set of Items is RMB1,000)'),
         ('2711F41', '0055', '旅行证件重置费用\nLoss of Travel document'), ('2711F43', '0057', '个人责任\nPersonal Liability'),
         ('2711F44', '0058', '银行卡盗刷（不适用未成年人）\nBank Card Fradulent Usage(not applicable to minors)'), ('2711F45', '0059',
                                                                                                      '旅行期间家居物品保障（火灾、爆炸、盗窃导致的损失，每件/每套限1000元）\nHome Guard Coverage(Limit per item or set of items is RMB1, 000)'),
         ('2711F30', '0043', '紧急医疗运送及送返 \nMedical evacuation and repatriation'), ('2711F31', '0044',
                                                                                  '遗体或骨灰送返（灵柩费限额6000元，丧葬费用以20,000元为限）\nRepatriation or Cremains of Remains （Cremains Expenses Limited to RMB6,000,Funeral Fxpenses Limited to 20000）'),
         ('2711F32', '0045', '亲属前往慰问探访\nRelative Visit'), ('2711F46', '0060', '未成年人送返\nReturn of Minors')]
        ,
        '''1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
All the terms and conditions subject to the official issued policy wording of Hyundai Insurance (China) Co., Ltd.
2.本计划的承保年龄为1至80周岁,以保单生效时的周岁年龄为准。65至80周岁的被保险人，其涉及“意外身故、残疾保障、意外医疗费用”保险金额为上表所载金额的一半,保险费维持不变。
Age Limit is 1 - 80 years old which shall be determined upon entry into force of insurance policy.  The sum insured of AD&D，Common Carrier Personal Accident，and Medical Expense will be 50% as stipulated above for the insured person aged 65 to 80.
3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。
According to CIRC, the sum Insured of the accumulative death of shall not exceed RMB 200,000 and RMB500, 000 for minors under 10 years old & minors aged 10 to 17 respectively. If the insured amount exceeds the pre-said provisions, the amount insured shall be limited to the named sum insured.The amount of accidental death insurance for aviation accident and the amount of accidental death insurance of natural disasters shall not be subject to this limit.
4.在同一保险期间内，每位被保险人仅限投保一份旅行意外伤害保险。若同一个被保险人就同一旅行同时投保2份（或以上）任何旅游险产品，则仅按保额最高者作出赔偿。
During the same insurance period, each insured person will be limited for a single plan. If an insured person who purchases 2 insurance plans for the same trip, the insurer will indemnify subject to the plan with a higher sum insured.
5.被保险人的法定住所地或经常居住地须位于中国大陆(外籍含港澳台人士理赔时须提供中国大陆的居留证或工作证明，连续居住时间≥6个月，不承保回原国籍)，旅行行程开始和终止于中国大陆。
The foreigner (excluding nationality of Hong Kong, Macau and Taiwan) in China who would like to purchase this insurance scheme must own working or residences permit. The policy does not cover the return of original nationality of the insured person.
6.境外旅行期间内因罹患突发疾病或遭受意外伤害而导致严重身体伤害，或预订的返回其日常居住地的公共交通工具由于不可抗力的原因导致延误，无法如期回到其日常居住地，保险人将根据被保险人完成该次旅行合理及必需的时间自动延长保险期间，最高可延期7天。
With a serious bodily damage by sudden illness or accidental injury during travel abroad or the delays arising from the scheduled public transport returning to their daily residence due to force majeure, the insured person cannot return to their daily residence on schedule. The insurers shall automatically extend the insurance period for the reasonable and necessary time of completion of this trip of the insured person with the maximum of extension of the policy period up to 7 days.
7. 除外不保国家约定：
保险人将不对于联合国、欧洲国家、美国政府（SDN清单）、或法国政府制裁的个人、企业，领土、国家或组织，进行或提供活；或是前述对象无论直接或间接地和列为制裁的国家（如朝鲜、苏丹、叙利亚、古巴、克里米亚、伊拉克、阿富汗、巴基斯坦、萨赫勒地区：毛里塔尼亚，马里，尼日尔、也门、索马里等）进行的特别的活动一样适用制裁的规定。国家、领土、组织和个人的相关资料由法国经济和财政部公布，并可能根据国际情况加以改变。
双方同意并理解，任何涉及直接或间接联系受制裁个人、实体、领土、国家或组织的活动由都将不会由保险人执行，且合同中没有任何条款可针对或影响违反制裁制度规则的规定。保险人将不会因这项不执行而承担任何赔偿或赔偿责任或义务。
The Insured is not to process or otherwise engage activity for or on behalf of a sanctioned individual, entity, territory, country or organization targeted by the  United Nations, European or United States authorities (“SDN Lists”) or other applicable sanctions regime (limitation, embargo, freezing of assets or control) in particular activity involving directly or indirectly countries listed as a Sanctioned Countries (i.e. North Korea, Sudan, Syria, Cuba and Crimea, Iraq, Afghanistan, Pakistan, The Sahel Region:  Mauritania, Mali, Niger, Yemen, Somalia.)  (“hereinafter called the Sanctions regime).
The relevant information of the detailed countries, territories, organizations and individuals is published by the French Ministere de l’Economie et des Finances and may change according to the international context.
It is agreed and understood that any action that implies a direct or indirect connection to a sanctioned individual, entity, territory, country or organization could be implemented by the Insurer and no provision in the contract can have for object or effect a violation of the Sanctions regime rules will not be implemented by the Insurer and the Insurer will incur no liability or obligation to pay remedies or indemnities whatsoever because of this non-implementation.
8.本产品承保下列高风险运动:海拔6000米以下的休闲旅游、远足徒步、登山运动、山地穿越、露营、自行车运动、山地自行车越野、场地/越野轮滑、自驾车旅行;游泳、潜水(下潜深度不超过18米)、溯溪、划船、帆船、帆板、皮划艇、漂流;人工/自然场地攀岩及下降、固定路线洞穴体验、野外生存、徒步穿越无人区(沙漠、戈壁等);定向运动、拓展活动、场地趣味活动、攀冰、滑雪运动、骑马游玩、马术培训、马术比赛(竞速赛、绕桶赛)、丛林飞跃、飞盘、TUTU车、溯溪、高海拔登山、攀冰、海上摩托、速降。
This insurance covers the following high risk sports: an elevation of 6000 meters below the leisure tourism, hiking, mountaineering, hiking, camping, mountain crossing fixed route cave experience, wilderness survival, hiking through the uninhabited areas (desert and Gobi); Orienteering activities, fun activities, field cycling, mountain bike cross-country site / off-road skating, self-driving travel; swimming and diving (depth of less than 18 meters), canyoning, rowing, sailing, windsurfing, kayaking, rafting and climbing venues; artificial / natural decline, climbing, skiing, horseback riding, equestrian training, play equestrian (sprint, barrel racing), jungle leap, Tutu car,  Frisbee, canyoning, mountaineering, climbing, rappelling.
9.关于隐私和利益保护:被保险人在购买本保险产品时提供的个人资料，如：姓名、性别、年龄、出生日期、身份证号等，保险公司将通过各种安全技术和程序来保护用户的上述个人信息不被未经授权的访问、使用或泄露。并承诺未经用户同意不会将用户的任何资料以任何方式泄露给任何第三方，符合法律要求或本保险公司的相关服务条款、软件许可使用协议等约定的除外。
Regarding privacy and protection of interests: 
Personal data provided by insured person when purchasing insurance product such as name sex age birth date ID card number etc. The Insurer will protect insured personal information from unauthorized access, use or disclosure through various security technologies and procedures. The insurer also promises not to disclose any information to any third party without user consent unless otherwise agreed upon by law or insurance company''s relevant terms of service or software license usage agreement etc.
10.旅程延误(300元/每5小时);
行李延误(500元/每8小时);
个人行李（每件或每套行李最高赔偿额为RMB1,000元）;
旅行期间家居物品保障（火灾、爆炸、盗窃导致的损失，每件/每套限1000元）
遗体或骨灰送返（灵柩费限额6000元，丧葬费用以20,000元为限）
Travel Delay(￥300/per 5 hours)
Baggage Delay(￥500/per 8 hours);
Baggage Loss or Damage(Limit per item or set of items is RMB1, 000);
Home Guard Coverage(Limit per item or set of items is RMB1, 000);
Repatriation or Cremains of Remains （Cremains
Expenses Limited to RMB6,000,Funeral Fxpenses Limited to 20000）
11.若英文译本与中文有异，以中文版为准。
Should there be any inconsistency between Chinese and English versions, the Chinese version shall prevail.'''
    ],
    [
        'P272018BCJJ000602',
        '高端版',
        2853600.00,
        [('2711C03', '0046',
          '意外身故，残疾及烧伤(含旅行期间高风险运动保障、酒店意外身故保障、地震意外身故保障、海啸意外身故)\nAccidental Death and Disablement & Burns (Include Accidental Death due to hotel-stay, earthquake, tsunami)'),
         ('2711F28', '0041',
          '公共交通工具意外身故、残疾(包含摩托车意外身故保障、长途公共汽车意外身故保障)\nCommon Carrier Accident (Include Accidental Death due to motorbike-drive, long-distance coach)'),
         ('2711F33', '0047', '医疗费用补偿（含意外和急性病）\nMedical Expenses - Outpatient (due to accident & acute disease) '), (
         '2711F34', '0048',
         '住院津贴（含意外和急性病）50元/天（最高30天）\nMedical Expenses - Inpatient (due to accident & acute disease) RMB ¥50/per day (most 30 days)'),
         ('2711F47', '0061', '突发急性病身故\nDeath due to Acute Disease'),
         ('2711F48', '0062', '自驾车意外身故及残疾\nAccidental Death and Disablement due to self-drive'),
         ('2711F38', '0052', '旅程延误(300元/每5小时)\nTravel Delay(¥300/per 5 hours)'),
         ('2711F39', '0053', '行李延误(500元/每8小时)\nBaggage Delay(¥500/per 8 hours)'),
         ('2711F40', '0054', '旅行取消/变更\nTrip Cancellation'), ('2711F06', '0007',
                                                             '个人行李（每件或每套行李最高赔偿额为RMB1,000元）\nBaggage Loss or Damage(Limit Per Item or Set of Items is RMB1,000)'),
         ('2711F41', '0055', '旅行证件重置费用\nLoss of Travel document'), ('2711F43', '0057', '个人责任\nPersonal Liability'),
         ('2711F44', '0058', '银行卡盗刷（不适用未成年人）\nBank Card Fradulent Usage(not applicable to minors)'), ('2711F45', '0059',
                                                                                                      '旅行期间家居物品保障（火灾、爆炸、盗窃导致的损失，每件/每套限1000元）\nHome Guard Coverage(Limit per item or set of items is RMB1, 000)'),
         ('2711F30', '0043', '紧急医疗运送及送返 \nMedical evacuation and repatriation'), ('2711F31', '0044',
                                                                                  '遗体或骨灰送返（灵柩费限额6000元，丧葬费用以20,000元为限）\nRepatriation or Cremains of Remains （Cremains Expenses Limited to RMB6,000,Funeral Fxpenses Limited to 20000）'),
         ('2711F32', '0045', '亲属前往慰问探访\nRelative Visit'), ('2711F46', '0060', '未成年人送返\nReturn of Minors')]
        ,
        '''1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
All the terms and conditions subject to the official issued policy wording of Hyundai Insurance (China) Co., Ltd.
2.本计划的承保年龄为1至80周岁,以保单生效时的周岁年龄为准。65至80周岁的被保险人，其涉及“意外身故、残疾保障、意外医疗费用”保险金额为上表所载金额的一半,保险费维持不变。
Age Limit is 1 - 80 years old which shall be determined upon entry into force of insurance policy.  The sum insured of AD&D，Common Carrier Personal Accident，and Medical Expense will be 50% as stipulated above for the insured person aged 65 to 80.
3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。
According to CIRC, the sum Insured of the accumulative death of shall not exceed RMB 200,000 and RMB500, 000 for minors under 10 years old & minors aged 10 to 17 respectively. If the insured amount exceeds the pre-said provisions, the amount insured shall be limited to the named sum insured.The amount of accidental death insurance for aviation accident and the amount of accidental death insurance of natural disasters shall not be subject to this limit.
4.在同一保险期间内，每位被保险人仅限投保一份旅行意外伤害保险。若同一个被保险人就同一旅行同时投保2份（或以上）任何旅游险产品，则仅按保额最高者作出赔偿。
During the same insurance period, each insured person will be limited for a single plan. If an insured person who purchases 2 insurance plans for the same trip, the insurer will indemnify subject to the plan with a higher sum insured.
5.被保险人的法定住所地或经常居住地须位于中国大陆(外籍含港澳台人士理赔时须提供中国大陆的居留证或工作证明，连续居住时间≥6个月，不承保回原国籍)，旅行行程开始和终止于中国大陆。
The foreigner (excluding nationality of Hong Kong, Macau and Taiwan) in China who would like to purchase this insurance scheme must own working or residences permit. The policy does not cover the return of original nationality of the insured person.
6.境外旅行期间内因罹患突发疾病或遭受意外伤害而导致严重身体伤害，或预订的返回其日常居住地的公共交通工具由于不可抗力的原因导致延误，无法如期回到其日常居住地，保险人将根据被保险人完成该次旅行合理及必需的时间自动延长保险期间，最高可延期7天。
With a serious bodily damage by sudden illness or accidental injury during travel abroad or the delays arising from the scheduled public transport returning to their daily residence due to force majeure, the insured person cannot return to their daily residence on schedule. The insurers shall automatically extend the insurance period for the reasonable and necessary time of completion of this trip of the insured person with the maximum of extension of the policy period up to 7 days.
7. 除外不保国家约定：
保险人将不对于联合国、欧洲国家、美国政府（SDN清单）、或法国政府制裁的个人、企业，领土、国家或组织，进行或提供活；或是前述对象无论直接或间接地和列为制裁的国家（如朝鲜、苏丹、叙利亚、古巴、克里米亚、伊拉克、阿富汗、巴基斯坦、萨赫勒地区：毛里塔尼亚，马里，尼日尔、也门、索马里等）进行的特别的活动一样适用制裁的规定。国家、领土、组织和个人的相关资料由法国经济和财政部公布，并可能根据国际情况加以改变。
双方同意并理解，任何涉及直接或间接联系受制裁个人、实体、领土、国家或组织的活动由都将不会由保险人执行，且合同中没有任何条款可针对或影响违反制裁制度规则的规定。保险人将不会因这项不执行而承担任何赔偿或赔偿责任或义务。
The Insured is not to process or otherwise engage activity for or on behalf of a sanctioned individual, entity, territory, country or organization targeted by the  United Nations, European or United States authorities (“SDN Lists”) or other applicable sanctions regime (limitation, embargo, freezing of assets or control) in particular activity involving directly or indirectly countries listed as a Sanctioned Countries (i.e. North Korea, Sudan, Syria, Cuba and Crimea, Iraq, Afghanistan, Pakistan, The Sahel Region:  Mauritania, Mali, Niger, Yemen, Somalia.)  (“hereinafter called the Sanctions regime).
The relevant information of the detailed countries, territories, organizations and individuals is published by the French Ministere de l’Economie et des Finances and may change according to the international context.
It is agreed and understood that any action that implies a direct or indirect connection to a sanctioned individual, entity, territory, country or organization could be implemented by the Insurer and no provision in the contract can have for object or effect a violation of the Sanctions regime rules will not be implemented by the Insurer and the Insurer will incur no liability or obligation to pay remedies or indemnities whatsoever because of this non-implementation.
8.本产品承保下列高风险运动:海拔6000米以下的休闲旅游、远足徒步、登山运动、山地穿越、露营、自行车运动、山地自行车越野、场地/越野轮滑、自驾车旅行;游泳、潜水(下潜深度不超过18米)、溯溪、划船、帆船、帆板、皮划艇、漂流;人工/自然场地攀岩及下降、固定路线洞穴体验、野外生存、徒步穿越无人区(沙漠、戈壁等);定向运动、拓展活动、场地趣味活动、攀冰、滑雪运动、骑马游玩、马术培训、马术比赛(竞速赛、绕桶赛)、丛林飞跃、飞盘、TUTU车、溯溪、高海拔登山、攀冰、海上摩托、速降。
This insurance covers the following high risk sports: an elevation of 6000 meters below the leisure tourism, hiking, mountaineering, hiking, camping, mountain crossing fixed route cave experience, wilderness survival, hiking through the uninhabited areas (desert and Gobi); Orienteering activities, fun activities, field cycling, mountain bike cross-country site / off-road skating, self-driving travel; swimming and diving (depth of less than 18 meters), canyoning, rowing, sailing, windsurfing, kayaking, rafting and climbing venues; artificial / natural decline, climbing, skiing, horseback riding, equestrian training, play equestrian (sprint, barrel racing), jungle leap, Tutu car,  Frisbee, canyoning, mountaineering, climbing, rappelling.
9.关于隐私和利益保护:被保险人在购买本保险产品时提供的个人资料，如：姓名、性别、年龄、出生日期、身份证号等，保险公司将通过各种安全技术和程序来保护用户的上述个人信息不被未经授权的访问、使用或泄露。并承诺未经用户同意不会将用户的任何资料以任何方式泄露给任何第三方，符合法律要求或本保险公司的相关服务条款、软件许可使用协议等约定的除外。
Regarding privacy and protection of interests: 
Personal data provided by insured person when purchasing insurance product such as name sex age birth date ID card number etc. The Insurer will protect insured personal information from unauthorized access, use or disclosure through various security technologies and procedures. The insurer also promises not to disclose any information to any third party without user consent unless otherwise agreed upon by law or insurance company''s relevant terms of service or software license usage agreement etc.
10.旅程延误(300元/每5小时);
行李延误(500元/每8小时);
个人行李（每件或每套行李最高赔偿额为RMB1,000元）;
旅行期间家居物品保障（火灾、爆炸、盗窃导致的损失，每件/每套限1000元）
遗体或骨灰送返（灵柩费限额6000元，丧葬费用以20,000元为限）
Travel Delay(￥300/per 5 hours)
Baggage Delay(￥500/per 8 hours);
Baggage Loss or Damage(Limit per item or set of items is RMB1, 000);
Home Guard Coverage(Limit per item or set of items is RMB1, 000);
Repatriation or Cremains of Remains （Cremains
Expenses Limited to RMB6,000,Funeral Fxpenses Limited to 20000）
11.若英文译本与中文有异，以中文版为准。
Should there be any inconsistency between Chinese and English versions, the Chinese version shall prevail.'''
    ]

]

seq_no = 1;

out_file = open('./sql_script/' + RISK_CODE + "_" + PRODCUT_CODE + "_" + PRODCUT_NAME + '_PRODUCT.sql', 'wt',
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
    chk_out_file = open('./sql_script/' + RISK_CODE + "_" + plan[0] + "_" + plan[1] + '_INFCHK.sql', 'wt',
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

    eploicy_out_file = open('./sql_script/' + RISK_CODE + "_" + plan[0] + "_" + plan[1] + '_EPOLICY.sql',
                            'wt',
                            encoding='utf-8')

    eploicy_out_file.write(EPOLICY_TMPL.format(plan[0], RISK_NAME))
    eploicy_out_file.close()

out_file.close()



/****

GEN_DATE = '23-04-2018'
AGENT_CODE = 'M00000000008'
AGENT_AGREEN = 'M00000000008-03'
RISK_CODE = '2701'
RISK_NAME = '个人境外旅行保险'
PRODCUT_CODE = 'P272018JTJJ0005'
PRODCUT_NAME = '个人境外旅游意外险-基本款'
PLAN_LIST = [['P272018JTJJ000501', '个人境外旅游意外险-基本款-方案一', 719000.0, [('2701C01', '0001'), ('2701F26', '0036'), ('2701F27', '0037'), ('2701F28', '0038'), ('2701F29', '0039'), ('2701F03', '0004'), ('2701F04', '0005'), ('2701F16', '0017')], '特别约定：\n1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。\n2.本计划的承保年龄为30天至85周岁,以保单生效时的周岁年龄为准。61周岁（含）以上人员投保，保额不变，保费为标准保费的2倍。      \n3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。\n4.本产品承保区域为全球（包括中国境内、且含香港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游目的地国家和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告为紧急状态的国家和地区。\n5.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求,但不承保回原国籍。\n6.本保险产品中高风险运动按照《附加高风险运动意外伤害保险条款》中对高风险运动的释义约定执行，但不承保海拔4500米以上的攀登、高山滑翔、极地探险,非固定路线洞穴探险、蹦极、攀岩/攀冰运动、自由式潜水(下潜深度超过18米,无水下呼吸设备)、赛车、赛马、跳伞、滑翔翼、极速运动等高风险探险类活动。\n7.本产品可提供24小时紧急救援服务及紧急医疗咨询服务，全球24小时救援电话号码:  \n8.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。\n9.本产品限购3份，但叠加保额只针对意外伤害主险。']]
*/
-- 产品信息
insert into prpdproduct (PRODUCTCODE, PRODUCTNAME, AGENTCODE, VALIDSTATUS, NOTE, NOTE1, NOTE2, NOTE3, OPERATORCODE, OPERATORDATE, UPDATECODE, UPDATEDATE, NOTE4)values ('P272018JTJJ0005', '个人境外旅游意外险-基本款', 'M00000000008', '1', '', '', '', '106', '0000000610', to_date('23-04-2018', 'dd-mm-yyyy'), '0000000610', to_date('23-04-2018', 'dd-mm-yyyy'), '');
insert into prpdproductrisk (PRODUCTCODE, RISKCODE, RISKCODENAME, OPERATORCODE, OPERATORDATE) values ('P272018JTJJ0005', '2701', '个人境外旅行保险', '0000000610', to_date('23-04-2018', 'dd-mm-yyyy'));


-- 方案信息  

-- 方案信息 - 个人境外旅游意外险-基本款-方案一
insert into prpdprogramme (PRODUCTCODE, PROGRAMMECODE, PROGRAMMENAME, SUMAMOUNT, OPERATORCODE, OPERATORDATE) values ('P272018JTJJ0005', 'P272018JTJJ000501', '个人境外旅游意外险-基本款-方案一', 719000.0, '0000000610', to_date('23-04-2018', 'dd-mm-yyyy'));
insert into prpdcode (CODETYPE, CODECODE, CODECNAME, CODEENAME, NEWCODECODE, VALIDSTATUS, FLAG) values ('Plancodemappped', 'P272018JTJJ000501', '个人境外旅游意外险-基本款-方案一', 'M00000000008-03', 'P272018JTJJ000501', '1', '1');

-- 方案信息 - 保障责任关联
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2701', 'P272018JTJJ000501', '2701C01', '0001', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2701', 'P272018JTJJ000501', '2701F26', '0036', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2701', 'P272018JTJJ000501', '2701F27', '0037', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2701', 'P272018JTJJ000501', '2701F28', '0038', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2701', 'P272018JTJJ000501', '2701F29', '0039', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2701', 'P272018JTJJ000501', '2701F03', '0004', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2701', 'P272018JTJJ000501', '2701F04', '0005', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2701', 'P272018JTJJ000501', '2701F16', '0017', null);


-- 方案信息 - 特别约定
/*
特别约定：
1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
2.本计划的承保年龄为30天至85周岁,以保单生效时的周岁年龄为准。61周岁（含）以上人员投保，保额不变，保费为标准保费的2倍。      
3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。
4.本产品承保区域为全球（包括中国境内、且含香港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游目的地国家和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告为紧急状态的国家和地区。
5.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求,但不承保回原国籍。
6.本保险产品中高风险运动按照《附加高风险运动意外伤害保险条款》中对高风险运动的释义约定执行，但不承保海拔4500米以上的攀登、高山滑翔、极地探险,非固定路线洞穴探险、蹦极、攀岩/攀冰运动、自由式潜水(下潜深度超过18米,无水下呼吸设备)、赛车、赛马、跳伞、滑翔翼、极速运动等高风险探险类活动。
7.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。
8.本产品限购3份，但叠加保额只针对意外伤害主险。
9.江泰客服电话：400-616-1188
*/


DELETE FROM PRPDENGAGE WHERE CLAUSECODE = 'T0P272018JTJJ000501';
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',1,'T0P272018JTJJ000501','特别约定：
1.所有的保险责任及条款均以现代财产保险(中国)有限公司签',0,0);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',2,'T0P272018JTJJ000501','发的正式保险合同之相应条款为准。
2.本计划的承保年龄为30天至85周',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',3,'T0P272018JTJJ000501','岁,以保单生效时的周岁年龄为准。61周岁（含）以上人员投保，保额不变，',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',4,'T0P272018JTJJ000501','保费为标准保费的2倍。      
3.按中国保监会规定,10周岁以下',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',5,'T0P272018JTJJ000501','的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',6,'T0P272018JTJJ000501','年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',7,'T0P272018JTJJ000501','超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',8,'T0P272018JTJJ000501','然灾害意外死亡保险金额不受此限。
4.本产品承保区域为全球（包括中国境',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',9,'T0P272018JTJJ000501','内、且含香港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',10,'T0P272018JTJJ000501','目的地国家和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',11,'T0P272018JTJJ000501','为紧急状态的国家和地区。
5.外籍人士购买本产品只要符合投保规则即可,',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',12,'T0P272018JTJJ000501','无其它特殊要求,但不承保回原国籍。
6.本保险产品中高风险运动按照《附',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',13,'T0P272018JTJJ000501','加高风险运动意外伤害保险条款》中对高风险运动的释义约定执行，但不承保海',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',14,'T0P272018JTJJ000501','拔4500米以上的攀登、高山滑翔、极地探险,非固定路线洞穴探险、蹦极、',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',15,'T0P272018JTJJ000501','攀岩/攀冰运动、自由式潜水(下潜深度超过18米,无水下呼吸设备)、赛车',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',16,'T0P272018JTJJ000501','、赛马、跳伞、滑翔翼、极速运动等高风险探险类活动。
7.本产品可提供2',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',17,'T0P272018JTJJ000501','4小时紧急救援服务及紧急医疗咨询服务，全球24小时救援电话号码:  
',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',18,'T0P272018JTJJ000501','8.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',19,'T0P272018JTJJ000501','险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',20,'T0P272018JTJJ000501','要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',21,'T0P272018JTJJ000501','禁止的线路或地区等。
9.本产品限购3份，但叠加保额只针对意外伤害主险',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2701',22,'T0P272018JTJJ000501','。',1,1);



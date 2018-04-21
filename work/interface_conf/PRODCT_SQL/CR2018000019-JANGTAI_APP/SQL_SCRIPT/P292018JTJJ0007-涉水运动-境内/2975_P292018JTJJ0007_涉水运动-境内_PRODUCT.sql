/****

GEN_DATE = '21-04-2018'
AGENT_CODE = 'M00000000008'
AGENT_AGREEN = 'M00000000008-01'
RISK_CODE = '2975'
RISK_NAME = '户外人身意外伤害保险'
PRODCUT_CODE = 'P292018JTJJ0007'
PRODCUT_NAME = '涉水运动-境内'
PLAN_LIST = [['P292018JTJJ000701', '涉水运动-境内-方案一', 239000.0, [('2975C01', '001'), ('2975F12', '013'), ('2975F32', '033'), ('2975F14', '015'), ('2975F13', '014'), ('2975F07', '008')], '特别约定：\n1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。\n2.本计划的承保年龄为18至65周岁,以保单生效时的周岁年龄为准。60周岁以上的被保险人,其涉及“意外身故、残疾保障”、“急性病身故保障”、“医疗费用保障”保险金额为上表所载金额的一半,保险费维持不变。\n3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。\n4.本产品承保区域为全球（包括中国境内、且含香港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游目的地国家和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告为紧急状态的国家和地区。or本产品仅承保在中国大陆地区（不包含香港、澳门及台湾）发生的意外伤害事故。\n5.本保险产品承保在合法经营场地内进行的溯溪、漂流、浮潜、快艇水上运动期间的保险责任。\n6.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求。\n7.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。\n8.本产品限购3份，但叠加保额只针对意外伤害主险。']]
*/
-- 产品信息
insert into prpdproduct (PRODUCTCODE, PRODUCTNAME, AGENTCODE, VALIDSTATUS, NOTE, NOTE1, NOTE2, NOTE3, OPERATORCODE, OPERATORDATE, UPDATECODE, UPDATEDATE, NOTE4)values ('P292018JTJJ0007', '涉水运动-境内', 'M00000000008', '1', '', '', '', '106', '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'), '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'), '');
insert into prpdproductrisk (PRODUCTCODE, RISKCODE, RISKCODENAME, OPERATORCODE, OPERATORDATE) values ('P292018JTJJ0007', '2975', '户外人身意外伤害保险', '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'));


-- 方案信息  

-- 方案信息 - 涉水运动-境内-方案一
insert into prpdprogramme (PRODUCTCODE, PROGRAMMECODE, PROGRAMMENAME, SUMAMOUNT, OPERATORCODE, OPERATORDATE) values ('P292018JTJJ0007', 'P292018JTJJ000701', '涉水运动-境内-方案一', 239000.0, '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'));
insert into prpdcode (CODETYPE, CODECODE, CODECNAME, CODEENAME, NEWCODECODE, VALIDSTATUS, FLAG) values ('Plancodemappped', 'P292018JTJJ000701', '涉水运动-境内-方案一', 'M00000000008-01', 'P292018JTJJ000701', '1', '1');

-- 方案信息 - 保障责任关联
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ000701', '2975C01', '001', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ000701', '2975F12', '013', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ000701', '2975F32', '033', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ000701', '2975F14', '015', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ000701', '2975F13', '014', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ000701', '2975F07', '008', null);


-- 方案信息 - 特别约定
/*
特别约定：
1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
2.本计划的承保年龄为18至65周岁,以保单生效时的周岁年龄为准。60周岁以上的被保险人,其涉及“意外身故、残疾保障”、“急性病身故保障”、“医疗费用保障”保险金额为上表所载金额的一半,保险费维持不变。
3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。
4.本产品承保区域为全球（包括中国境内、且含香港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游目的地国家和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告为紧急状态的国家和地区。or本产品仅承保在中国大陆地区（不包含香港、澳门及台湾）发生的意外伤害事故。
5.本保险产品承保在合法经营场地内进行的溯溪、漂流、浮潜、快艇水上运动期间的保险责任。
6.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求。
7.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。
8.本产品限购3份，但叠加保额只针对意外伤害主险。
*/


DELETE FROM PRPDENGAGE WHERE CLAUSECODE = 'TOP292018JTJJ000701';
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',1,'T0P292018JTJJ000701','特别约定：
1.所有的保险责任及条款均以现代财产保险(中国)有限公司签',0,0);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',2,'T0P292018JTJJ000701','发的正式保险合同之相应条款为准。
2.本计划的承保年龄为18至65周岁',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',3,'T0P292018JTJJ000701',',以保单生效时的周岁年龄为准。60周岁以上的被保险人,其涉及“意外身故',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',4,'T0P292018JTJJ000701','、残疾保障”、“急性病身故保障”、“医疗费用保障”保险金额为上表所载金',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',5,'T0P292018JTJJ000701','额的一半,保险费维持不变。
3.按中国保监会规定,10周岁以下的未成年',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',6,'T0P292018JTJJ000701','人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',7,'T0P292018JTJJ000701','身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',8,'T0P292018JTJJ000701','规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',9,'T0P292018JTJJ000701','外死亡保险金额不受此限。
4.本产品承保区域为全球（包括中国境内、且含',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',10,'T0P292018JTJJ000701','香港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游目的地国',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',11,'T0P292018JTJJ000701','家和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告为紧急状',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',12,'T0P292018JTJJ000701','态的国家和地区。or本产品仅承保在中国大陆地区（不包含香港、澳门及台湾',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',13,'T0P292018JTJJ000701','）发生的意外伤害事故。
5.本保险产品承保在合法经营场地内进行的溯溪、',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',14,'T0P292018JTJJ000701','漂流、浮潜、快艇水上运动期间的保险责任。
6.外籍人士购买本产品只要符',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',15,'T0P292018JTJJ000701','合投保规则即可,无其它特殊要求。
7.被保险人故意做出的危险性行为而导',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',16,'T0P292018JTJJ000701','致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',17,'T0P292018JTJJ000701','从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',18,'T0P292018JTJJ000701','令标示；违规进入国家或当地政府明令禁止的线路或地区等。
8.本产品限购',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',19,'T0P292018JTJJ000701','3份，但叠加保额只针对意外伤害主险。',1,1);



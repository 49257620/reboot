/****

GEN_DATE = '21-04-2018'
AGENT_CODE = 'M00000000008'
AGENT_AGREEN = 'M00000000008-01'
RISK_CODE = '2975'
RISK_NAME = '户外人身意外伤害保险'
PRODCUT_CODE = 'P292018JTJJ0016'
PRODCUT_NAME = '赛事运动-境内'
PLAN_LIST = [['P292018JTJJ001601', '赛事运动-境内-方案一', 189000.0, [('2975C01', '001'), ('2975F32', '033'), ('2975F01', '002'), ('2975F13', '014'), ('2975F07', '008')], '特别约定：\n1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。\n2.本计划的承保年龄为3至80周岁,以保单生效时的周岁年龄为准。60周岁以上的被保险人,其涉及“意外身故、残疾保障”、“急性病身故保障”、“医疗费用保障”保险金额为上表所载金额的一半,保险费维持不变。\n3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。\n4.本产品承保区域为全球（包括中国境内、且含香港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游目的地国家和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告为紧急状态的国家和地区。or本产品仅承保在中国大陆地区（不包含香港、澳门及台湾）发生的意外伤害事故。\n5.本产品承保有固定路线的洞穴体验、野外生存、定向运动；场地自行车、山地自行车越野、场地/越野轮滑；帆船、帆板、皮划艇；人工/自然场地攀岩及下降、攀冰、滑雪运动；马术竞速/绕桶赛。\n6.本产品可承保有奖金的竞赛赛事，但不承保职业运动员，职业运动员是指与专业体育运动俱乐部签订合同,依靠工资,奖金和商业促销的收入谋生的运动员。 \n7.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求。\n8.本产品限购2份，但叠加保额只针对意外伤害主险。']]
*/
-- 产品信息
insert into prpdproduct (PRODUCTCODE, PRODUCTNAME, AGENTCODE, VALIDSTATUS, NOTE, NOTE1, NOTE2, NOTE3, OPERATORCODE, OPERATORDATE, UPDATECODE, UPDATEDATE, NOTE4)values ('P292018JTJJ0016', '赛事运动-境内', 'M00000000008', '1', '', '', '', '106', '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'), '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'), '');
insert into prpdproductrisk (PRODUCTCODE, RISKCODE, RISKCODENAME, OPERATORCODE, OPERATORDATE) values ('P292018JTJJ0016', '2975', '户外人身意外伤害保险', '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'));


-- 方案信息  

-- 方案信息 - 赛事运动-境内-方案一
insert into prpdprogramme (PRODUCTCODE, PROGRAMMECODE, PROGRAMMENAME, SUMAMOUNT, OPERATORCODE, OPERATORDATE) values ('P292018JTJJ0016', 'P292018JTJJ001601', '赛事运动-境内-方案一', 189000.0, '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'));
insert into prpdcode (CODETYPE, CODECODE, CODECNAME, CODEENAME, NEWCODECODE, VALIDSTATUS, FLAG) values ('Plancodemappped', 'P292018JTJJ001601', '赛事运动-境内-方案一', 'M00000000008-01', 'P292018JTJJ001601', '1', '1');

-- 方案信息 - 保障责任关联
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001601', '2975C01', '001', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001601', '2975F32', '033', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001601', '2975F01', '002', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001601', '2975F13', '014', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001601', '2975F07', '008', null);


-- 方案信息 - 特别约定
/*
特别约定：
1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
2.本计划的承保年龄为3至80周岁,以保单生效时的周岁年龄为准。60周岁以上的被保险人,其涉及“意外身故、残疾保障”、“急性病身故保障”、“医疗费用保障”保险金额为上表所载金额的一半,保险费维持不变。
3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。
4.本产品承保区域为全球（包括中国境内、且含香港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游目的地国家和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告为紧急状态的国家和地区。or本产品仅承保在中国大陆地区（不包含香港、澳门及台湾）发生的意外伤害事故。
5.本产品承保有固定路线的洞穴体验、野外生存、定向运动；场地自行车、山地自行车越野、场地/越野轮滑；帆船、帆板、皮划艇；人工/自然场地攀岩及下降、攀冰、滑雪运动；马术竞速/绕桶赛。
6.本产品可承保有奖金的竞赛赛事，但不承保职业运动员，职业运动员是指与专业体育运动俱乐部签订合同,依靠工资,奖金和商业促销的收入谋生的运动员。 
7.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求。
8.本产品限购2份，但叠加保额只针对意外伤害主险。
*/


DELETE FROM PRPDENGAGE WHERE CLAUSECODE = 'T0P292018JTJJ001601';
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',1,'T0P292018JTJJ001601','特别约定：
1.所有的保险责任及条款均以现代财产保险(中国)有限公司签',0,0);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',2,'T0P292018JTJJ001601','发的正式保险合同之相应条款为准。
2.本计划的承保年龄为3至80周岁,',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',3,'T0P292018JTJJ001601','以保单生效时的周岁年龄为准。60周岁以上的被保险人,其涉及“意外身故、',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',4,'T0P292018JTJJ001601','残疾保障”、“急性病身故保障”、“医疗费用保障”保险金额为上表所载金额',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',5,'T0P292018JTJJ001601','的一半,保险费维持不变。
3.按中国保监会规定,10周岁以下的未成年人',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',6,'T0P292018JTJJ001601','累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',7,'T0P292018JTJJ001601','故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',8,'T0P292018JTJJ001601','定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',9,'T0P292018JTJJ001601','死亡保险金额不受此限。
4.本产品承保区域为全球（包括中国境内、且含香',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',10,'T0P292018JTJJ001601','港、澳门、台湾地区），具体承保地域以国家旅游局公布的中国旅游目的地国家',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',11,'T0P292018JTJJ001601','和地区为准，但不包含在被保险人出发前已处于战争状态或已被宣告为紧急状态',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',12,'T0P292018JTJJ001601','的国家和地区。or本产品仅承保在中国大陆地区（不包含香港、澳门及台湾）',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',13,'T0P292018JTJJ001601','发生的意外伤害事故。
5.本产品承保有固定路线的洞穴体验、野外生存、定',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',14,'T0P292018JTJJ001601','向运动；场地自行车、山地自行车越野、场地/越野轮滑；帆船、帆板、皮划艇',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',15,'T0P292018JTJJ001601','；人工/自然场地攀岩及下降、攀冰、滑雪运动；马术竞速/绕桶赛。
6.本',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',16,'T0P292018JTJJ001601','产品可承保有奖金的竞赛赛事，但不承保职业运动员，职业运动员是指与专业体',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',17,'T0P292018JTJJ001601','育运动俱乐部签订合同,依靠工资,奖金和商业促销的收入谋生的运动员。 
',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',18,'T0P292018JTJJ001601','7.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求。
8.本产',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',19,'T0P292018JTJJ001601','品限购2份，但叠加保额只针对意外伤害主险。',1,1);



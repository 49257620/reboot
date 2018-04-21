/****

GEN_DATE = '21-04-2018'
AGENT_CODE = 'M00000000008'
AGENT_AGREEN = 'M00000000008-01'
RISK_CODE = '2975'
RISK_NAME = '户外人身意外伤害保险'
PRODCUT_CODE = 'P292018JTJJ0011'
PRODCUT_NAME = '境内拓展训练险'
PLAN_LIST = [['P292018JTJJ001101', '境内拓展训练险-方案一', 189000.0, [('2975C01', '001'), ('2975F32', '033'), ('2975F14', '015'), ('2975F13', '014'), ('2975F07', '008')], '特别约定：\n1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。\n2.本计划的承保年龄为18至60周岁,以保单生效时的周岁年龄为准。\n3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。\n4.本产品仅承保在中国大陆地区（不包含香港、澳门及台湾）发生的意外伤害事故。\n5.本保险产品承保拓展训练包括但不限于：雷区取水、无敌风火轮 、背摔、断桥、孤岛求生、有轨电车、鳄鱼潭、时速极限、高空拓展训练（不高于30米，且所有从事空中活动的人士，必须绑定安全带）、钻电网、真人CS、毕业墙、信任背摔、模拟电网、移花接木、罐头鞋、梅花桩、盲目障碍、礼让通行、齐心协力、雷阵、吊索桥、情侣桥、水上漂、搭板过河、板桥、缅甸桥、溜索过河、滚筒桥、秋千桥、云梯桥、栈道桥、索道桥等拓展训练期间的保险责任。\n6.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求。\n7.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。\n8.本产品限购3份，但叠加保额只针对意外伤害主险。']]
*/
-- 产品信息
insert into prpdproduct (PRODUCTCODE, PRODUCTNAME, AGENTCODE, VALIDSTATUS, NOTE, NOTE1, NOTE2, NOTE3, OPERATORCODE, OPERATORDATE, UPDATECODE, UPDATEDATE, NOTE4)values ('P292018JTJJ0011', '境内拓展训练险', 'M00000000008', '1', '', '', '', '106', '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'), '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'), '');
insert into prpdproductrisk (PRODUCTCODE, RISKCODE, RISKCODENAME, OPERATORCODE, OPERATORDATE) values ('P292018JTJJ0011', '2975', '户外人身意外伤害保险', '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'));


-- 方案信息  

-- 方案信息 - 境内拓展训练险-方案一
insert into prpdprogramme (PRODUCTCODE, PROGRAMMECODE, PROGRAMMENAME, SUMAMOUNT, OPERATORCODE, OPERATORDATE) values ('P292018JTJJ0011', 'P292018JTJJ001101', '境内拓展训练险-方案一', 189000.0, '0000000610', to_date('21-04-2018', 'dd-mm-yyyy'));
insert into prpdcode (CODETYPE, CODECODE, CODECNAME, CODEENAME, NEWCODECODE, VALIDSTATUS, FLAG) values ('Plancodemappped', 'P292018JTJJ001101', '境内拓展训练险-方案一', 'M00000000008-01', 'P292018JTJJ001101', '1', '1');

-- 方案信息 - 保障责任关联
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001101', '2975C01', '001', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001101', '2975F32', '033', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001101', '2975F14', '015', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001101', '2975F13', '014', null);
insert into prpdclausekind (RISKCODE, CLAUSETYPE, KINDCODE, RELATEKINDCODE, FLAG) values ('2975', 'P292018JTJJ001101', '2975F07', '008', null);


-- 方案信息 - 特别约定
/*
特别约定：
1.所有的保险责任及条款均以现代财产保险(中国)有限公司签发的正式保险合同之相应条款为准。
2.本计划的承保年龄为18至60周岁,以保单生效时的周岁年龄为准。
3.按中国保监会规定,10周岁以下的未成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾害意外死亡保险金额不受此限。
4.本产品仅承保在中国大陆地区（不包含香港、澳门及台湾）发生的意外伤害事故。
5.本保险产品承保拓展训练包括但不限于：雷区取水、无敌风火轮 、背摔、断桥、孤岛求生、有轨电车、鳄鱼潭、时速极限、高空拓展训练（不高于30米，且所有从事空中活动的人士，必须绑定安全带）、钻电网、真人CS、毕业墙、信任背摔、模拟电网、移花接木、罐头鞋、梅花桩、盲目障碍、礼让通行、齐心协力、雷阵、吊索桥、情侣桥、水上漂、搭板过河、板桥、缅甸桥、溜索过河、滚筒桥、秋千桥、云梯桥、栈道桥、索道桥等拓展训练期间的保险责任。
6.外籍人士购买本产品只要符合投保规则即可,无其它特殊要求。
7.被保险人故意做出的危险性行为而导致的意外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示；违规进入国家或当地政府明令禁止的线路或地区等。
8.本产品限购3份，但叠加保额只针对意外伤害主险。
*/


DELETE FROM PRPDENGAGE WHERE CLAUSECODE = 'TOP292018JTJJ001101';
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',1,'T0P292018JTJJ001101','特别约定：
1.所有的保险责任及条款均以现代财产保险(中国)有限公司签',0,0);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',2,'T0P292018JTJJ001101','发的正式保险合同之相应条款为准。
2.本计划的承保年龄为18至60周岁',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',3,'T0P292018JTJJ001101',',以保单生效时的周岁年龄为准。
3.按中国保监会规定,10周岁以下的未',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',4,'T0P292018JTJJ001101','成年人累计身故保险金额不得超过人民币20万元;10至17周岁的未成年人',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',5,'T0P292018JTJJ001101','累计身故保险金额不得超过人民币50万元。若未成年被保险人的保险金额超过',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',6,'T0P292018JTJJ001101','上述规定,则以上述规定的保险金额为限。航空意外死亡保险金额、重大自然灾',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',7,'T0P292018JTJJ001101','害意外死亡保险金额不受此限。
4.本产品仅承保在中国大陆地区（不包含香',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',8,'T0P292018JTJJ001101','港、澳门及台湾）发生的意外伤害事故。
5.本保险产品承保拓展训练包括但',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',9,'T0P292018JTJJ001101','不限于：雷区取水、无敌风火轮 、背摔、断桥、孤岛求生、有轨电车、鳄鱼潭',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',10,'T0P292018JTJJ001101','、时速极限、高空拓展训练（不高于30米，且所有从事空中活动的人士，必须',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',11,'T0P292018JTJJ001101','绑定安全带）、钻电网、真人CS、毕业墙、信任背摔、模拟电网、移花接木、',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',12,'T0P292018JTJJ001101','罐头鞋、梅花桩、盲目障碍、礼让通行、齐心协力、雷阵、吊索桥、情侣桥、水',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',13,'T0P292018JTJJ001101','上漂、搭板过河、板桥、缅甸桥、溜索过河、滚筒桥、秋千桥、云梯桥、栈道桥',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',14,'T0P292018JTJJ001101','、索道桥等拓展训练期间的保险责任。
6.外籍人士购买本产品只要符合投保',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',15,'T0P292018JTJJ001101','规则即可,无其它特殊要求。
7.被保险人故意做出的危险性行为而导致的意',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',16,'T0P292018JTJJ001101','外伤害事故，保险公司不承担保险责任，危险性行为包括但不限于：不听从导游',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',17,'T0P292018JTJJ001101','、领队、教练或现场安全人员的要求及劝阻；违反景区或当地的警示/禁令标示',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',18,'T0P292018JTJJ001101','；违规进入国家或当地政府明令禁止的线路或地区等。
8.本产品限购3份，',1,1);
INSERT INTO PRPDENGAGE (RISKCODE,SERIALNO,CLAUSECODE,CONTEXT,TITLEFLAG,FLAG) VALUES ('2975',19,'T0P292018JTJJ001101','但叠加保额只针对意外伤害主险。',1,1);



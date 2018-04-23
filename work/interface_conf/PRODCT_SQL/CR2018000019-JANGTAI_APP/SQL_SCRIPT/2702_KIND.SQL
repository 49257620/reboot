insert into prpdkind (RISKCODE, KINDCODE, KINDCNAME, KINDENAME, CALCULATEFLAG, NEWKINDCODE, VALIDSTATUS, FLAG) 
values ('2702', '2702C02', '个人境内旅行意外伤害保险/附加高风险运动意外伤害保险', null, 'Y11000', '2702C02', '1', '02');
insert into prpditem (RISKCODE, ITEMCODE, ITEMCNAME, ITEMENAME, ITEMFLAG, NEWITEMCODE, VALIDSTATUS, FLAG)
values ('2702', '027', '意外伤害身故或伤残保险金/高风险运动意外伤害身故或伤残保险金', null, 'N', '027', '1', null);
insert into prpdkinditem (RISKCODE, KINDCODE, ITEMCODE, FLAG)
values ('2702', '2702C02', '027', null);


insert into prpdkind (RISKCODE, KINDCODE, KINDCNAME, KINDENAME, CALCULATEFLAG, NEWKINDCODE, VALIDSTATUS, FLAG) 
values ('2702', '2702F26', '附加户外意外医疗保险', null, 'N12000', '2702F26', '1', '02');
insert into prpditem (RISKCODE, ITEMCODE, ITEMCNAME, ITEMENAME, ITEMFLAG, NEWITEMCODE, VALIDSTATUS, FLAG)
values ('2702', '028', '高风险运动意外伤害医疗保险金', null, 'N', '028', '1', null);
insert into prpdkinditem (RISKCODE, KINDCODE, ITEMCODE, FLAG)
values ('2702', '2702F26', '028', null);


insert into prpdkind (RISKCODE, KINDCODE, KINDCNAME, KINDENAME, CALCULATEFLAG, NEWKINDCODE, VALIDSTATUS, FLAG)
values ('2702', '2702F27', '附加境内旅行每日住院津贴保险/附加户外每日住院津贴保险条款', null, 'N12000', '2702F27', '1', '02');
insert into prpditem (RISKCODE, ITEMCODE, ITEMCNAME, ITEMENAME, ITEMFLAG, NEWITEMCODE, VALIDSTATUS, FLAG)
values ('2702', '029', '意外伤害、高风险运动意外伤害及急性病住院津贴保险金', null, 'N', '029', '1', null);
insert into prpdkinditem (RISKCODE, KINDCODE, ITEMCODE, FLAG)
values ('2702', '2702F27', '029', null);


insert into prpdkind (RISKCODE, KINDCODE, KINDCNAME, KINDENAME, CALCULATEFLAG, NEWKINDCODE, VALIDSTATUS, FLAG)
values ('2702', '2702F28', '附加个人责任保险条款', null, 'N12000', '2702F28', '1', '02');
insert into prpditem (RISKCODE, ITEMCODE, ITEMCNAME, ITEMENAME, ITEMFLAG, NEWITEMCODE, VALIDSTATUS, FLAG)
values ('2702', '030', '因个人原因导致第三者人身伤亡或财产直接损失', null, 'N', '030', '1', null);
insert into prpdkinditem (RISKCODE, KINDCODE, ITEMCODE, FLAG)
values ('2702', '2702F28', '030', null);


--PREMIUMRATIO
insert into PREMIUMRATIO (RISKCODE, MAINCOUNT, ACCECOUNT, MAINRATIO, ACCERATIO, OTHER1, OTHER2, OTHER3, OTHER4, AGENTCODE)
values ('2702', '1', '1,2,3,4,5,6,7,8,9,10', .65, .35, null, null, null, null,'M00000000008');
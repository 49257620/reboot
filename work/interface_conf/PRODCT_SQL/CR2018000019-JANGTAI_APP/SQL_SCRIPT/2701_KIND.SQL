
insert into prpdkind (RISKCODE, KINDCODE, KINDCNAME, KINDENAME, CALCULATEFLAG, NEWKINDCODE, VALIDSTATUS, FLAG) 
values ('2701', '2701F26', '附加高风险运动意外伤害保险', null, 'N12000', '2701F26', '1', '02');
insert into prpditem (RISKCODE, ITEMCODE, ITEMCNAME, ITEMENAME, ITEMFLAG, NEWITEMCODE, VALIDSTATUS, FLAG)
values ('2701', '0036', '高风险运动意外伤害身故或伤残', null, 'N', '0036', '1', null);
insert into prpdkinditem (RISKCODE, KINDCODE, ITEMCODE, FLAG)
values ('2701', '2701F26', '0036', null);

insert into prpdkind (RISKCODE, KINDCODE, KINDCNAME, KINDENAME, CALCULATEFLAG, NEWKINDCODE, VALIDSTATUS, FLAG)
values ('2701', '2701F27', '附加急性病身故或全残保险条款', null, 'N12000', '2701F27', '1', '02');
insert into prpditem (RISKCODE, ITEMCODE, ITEMCNAME, ITEMENAME, ITEMFLAG, NEWITEMCODE, VALIDSTATUS, FLAG)
values ('2701', '0037', '急性病身故（含猝死）及全残保险金', null, 'N', '0037', '1', null);
insert into prpdkinditem (RISKCODE, KINDCODE, ITEMCODE, FLAG)
values ('2701', '2701F27', '0037', null);

insert into prpdkind (RISKCODE, KINDCODE, KINDCNAME, KINDENAME, CALCULATEFLAG, NEWKINDCODE, VALIDSTATUS, FLAG)
values ('2701', '2701F28', '附加境外旅行医疗费用补偿保险/附加户外意外医疗保险', null, 'N12000', '2701F28', '1', '02');
insert into prpditem (RISKCODE, ITEMCODE, ITEMCNAME, ITEMENAME, ITEMFLAG, NEWITEMCODE, VALIDSTATUS, FLAG)
values ('2701', '0038', '意外伤害（含高风险运动）/急性病医疗费用保险金', null, 'N', '0038', '1', null);
insert into prpdkinditem (RISKCODE, KINDCODE, ITEMCODE, FLAG)
values ('2701', '2701F28', '0038', null);

insert into prpdkind (RISKCODE, KINDCODE, KINDCNAME, KINDENAME, CALCULATEFLAG, NEWKINDCODE, VALIDSTATUS, FLAG)
values ('2701', '2701F29', '附加境外旅行每日住院津贴保险条款', null, 'N12000', '2701F29', '1', '02');
insert into prpditem (RISKCODE, ITEMCODE, ITEMCNAME, ITEMENAME, ITEMFLAG, NEWITEMCODE, VALIDSTATUS, FLAG)
values ('2701', '0039', '意外伤害及急性病住院津贴', null, 'N', '0039', '1', null);
insert into prpdkinditem (RISKCODE, KINDCODE, ITEMCODE, FLAG)
values ('2701', '2701F29', '0039', null);



--PREMIUMRATIO
insert into PREMIUMRATIO (RISKCODE, MAINCOUNT, ACCECOUNT, MAINRATIO, ACCERATIO, OTHER1, OTHER2, OTHER3, OTHER4, AGENTCODE)
values ('2701', '1', '1,2,3,4,5,6,7,8,9,10', .65, .35, null, null, null, null,'M00000000008');
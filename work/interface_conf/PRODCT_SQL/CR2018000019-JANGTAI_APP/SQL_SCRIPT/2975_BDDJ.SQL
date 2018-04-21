INSERT INTO BDDJ_RISKCONFIG
	(CLASSCODE,   --险类如27
		RISKCODE,    --险种如2701
		AREA,
		RISKFLAG,
		EFFECTFLAG,  --有效标志 为1
		EFFECTDATE,   --插入时间
		INSUREDNATURE,
		IDV_UNIT,
		RISKCHANGE,
		RISKADD,   --产品新增标志 为1
		RISKDELETE,
		REMARK,
		RISKADDDATE,  --产品新增上报时间 具体到天
		RISKCHANGEDATE,
		RISKDELETEDATE)
VALUES
	('29',
		'2975',
		'1137',
		'3',
		'1         ',
		TO_DATE('24-04-2018', 'dd-mm-yyyy'),
		'3',
		'02',
		'0',
		'1',
		'0',
		'riskadd 只有产品新增填1 其他情况都是0 riskchange 只有产品变更填1 其他情况都是0 riskdelete 只有产品退市填1 其他情况都是0 ',
		TO_DATE('24-04-2018', 'dd-mm-yyyy'),
		NULL,
		NULL);
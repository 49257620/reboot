
INSERT INTO PRPDEPOLICYCONF (PRODCUTCODE, KEY, E_CODE, TYPE, POLICY_TYPE, IF_EMAIL, SIGN, EMAIL_MSG, EMAIL_HEAD, SHORT_MSG, CLAUSES, BASE_INFO_SQL, R1_USE_YN, R1_SQL, R2_USE_YN, R2_SQL, R3_USE_YN, R3_SQL, R4_USE_YN, R4_SQL, R5_USE_YN, R5_SQL) VALUES
('P272018JTJJ0005',
'E01',
'COTRACJT',
'A',
'COTRACJT',
'1',
'SM2',
'尊敬的{custName}:<br/>&nbsp;&nbsp;&nbsp;&nbsp;感谢您选择现代财产保险！您投保的保单号为：{policyNo}的保单已经投保成功，附件中是电子保单，请查收!<br/>&nbsp;&nbsp;&nbsp;&nbsp;欢迎您登陆我公司官网www.hi-ins.com.cn查询或拨打客服电话4006080808查询!',
'现代财产保险个人境外旅行保险电子保单',
'感谢您选择现代财产保险！您的保单号为：{policyNo}！欢迎您登陆我公司官网www.hi-ins.com.cn查询，或拨打客服电话4006080808查询！'
, null,
'select a.policyno V1 ,
        a.APPLINAME V2,
        c.PHONENUMBER V3,
        c.email V4,
        c.POSTADDRESS V5,
        c.POSTCODE V6,
        ''法定'' V7,
        ''个人境外旅行保险 电子保单'' V8,
        (a.ENDDATE - a.STARTDATE+1) V9,
        D.DESTINATIONAREA V10,
        TO_CHAR(a.STARTDATE,''YYYY'')||''年''||TO_CHAR(a.STARTDATE,''MM'')||''月''||TO_CHAR(a.STARTDATE,''DD'')||''日'' V11,
        a.STARTHOUR V12,
        TO_CHAR(a.ENDDATE,''YYYY'')||''年''||TO_CHAR(a.ENDDATE,''MM'')||''月''||TO_CHAR(a.ENDDATE,''DD'')||''日'' V13,
        ''24'' V14,
        a.SUMPREMIUM/a.SUMQUANTITY V15,
        a.SUMPREMIUM V16,
        '''' V17,
        '''' V18,
        '''' V19,
        '''' V20,
        '''' V21,
        '''' V22,
        '''' V23,
        '''' V24,
        '''' V25,
        '''' V26,
        '''' V27,
        '''' V28,
        '''' V29,
        '''' V30
 from prpcmain a ,prpcinsured c,PrpCtravelInfo D
 where a.policyno =''{policyNo}''
 and a.policyno = c.policyno
 AND A.POLICYNO = D.POLICYNO(+)
 and c.INSUREDFLAG=''2''                                                                                                                                                                                                                                                                                                                                                                             ', 1, 'select b.SUMQUANTITY RV1,
       a.INSUREDNAME RV2,
       c.CODECNAME RV3,
       a.IDENTIFYNUMBER RV4,
       a.sex RV5,
       a.BIRTHDAY RV6,
       a.age RV7,
       '''' RV8,
       '''' RV9,
       '''' RV10
from prpcinsured a,prpcmain b,PRPDCODE c
where a.POLICYNO =''{policyNo}''
and a.SERIALNO=''2''
and a.POLICYNO =  b.policyno
and c.codeType  =''IdentifyType''
and c.CODECODE =  a.IDENTIFYTYPE',
1,
'SELECT A.KINDCODE RV1,
       A.KINDNAME RV2,
       A.ITEMDETAILNAME RV3,
       SUM(AMOUNT) RV5,
       SUM(AMOUNT)/COUNT(DISTINCT A.FAMILYNAME) RV4,
       SUM(PREMIUM) RV7,
       SUM(PREMIUM)/COUNT(DISTINCT A.FAMILYNAME) RV6,
       trim(flag) RV8,
       '''' RV9,
       '''' RV10
FROM PRPCITEMKIND A
WHERE A.POLICYNO =''{policyNo}''
GROUP BY KINDCODE,A.KINDNAME,A.ITEMDETAILNAME ,flag
order by flag, KINDCODE',
1,
'select a.SERIALNO-1 RV1,
       a.INSUREDNAME RV2,
       c.CODECNAME RV3,
       a.IDENTIFYNUMBER RV4,
       a.sex RV5,
       to_char(a.BIRTHDAY,''YYYY-MM-DD'') RV6,
       a.age RV7,
       sum(D.amount) RV8,
       sum(D.premium) RV9,
       '''' RV10
from prpcinsured a,prpcmain b,PRPDCODE c,PRPCITEMKIND D
where a.POLICYNO =''{policyNo}''
and a.INSUREDFLAG=''1''
and a.POLICYNO =  b.policyno
and c.codeType  =''IdentifyType''
and c.CODECODE =  a.IDENTIFYTYPE
AND A.POLICYNO = D.POLICYNO
AND A.INSUREDNAME = D.FAMILYNAME
group by a.SERIALNO-1,
       a.INSUREDNAME,
       c.CODECNAME,
       a.IDENTIFYNUMBER,
       a.sex ,
       a.BIRTHDAY ,
       a.age
order by a.SERIALNO-1',
0,
null,
0,
null);

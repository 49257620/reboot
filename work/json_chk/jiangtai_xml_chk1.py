# encoding: utf-8
# Author: LW


from xml.etree import ElementTree as ET
import time
import math
import dbmanager as hicis

xml_str = """<root>
<agentCode>M00000000008</agentCode>
	<arbitBoardName>北京市仲裁委员会</arbitBoardName>
	<autoTransRenewFlag>3</autoTransRenewFlag>
	<businessNature>8</businessNature>
	<classCode>27</classCode>
	<endDate>2018-08-16T23:59:59</endDate>
	<operateDate>2018-08-10T10:37:10.363</operateDate>
	<orderId>FH180810103659508481</orderId>
	<planCode>2711002</planCode>
	<planFeeInfo>
		<currency>CNY</currency>
		<delinquentFee>518.9400</delinquentFee>
		<payNo>1</payNo>
		<payReason>R10</payReason>
		<planFee>518.9400</planFee>
		<serialNo>1</serialNo>
	</planFeeInfo>
	<policySort>0</policySort>
	<policyType>2</policyType>
	<profit1>1</profit1>
	<profit1Value>0.95</profit1Value>
	<profit2>1</profit2>
	<profit2Value>0.95</profit2Value>
	<proposalAppliInfo>
		<account />
		<bank />
		<email>yeyequna@163.com</email>
		<identifyNumber>91220201759332094N</identifyNumber>
		<identifyType>99</identifyType>
		<insuredAddress>吉林市昌邑区天江小区4号楼14号网点</insuredAddress>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>吉林市松花江国际旅行社有限责任公司</insuredName>
		<insuredNature>4</insuredNature>
		<invoicetype />
		<linkerName>王劢</linkerName>
		<mobile>13944211012</mobile>
		<nationalityCode>CHN</nationalityCode>
		<phoneNumber>13944211012</phoneNumber>
		<postAddress>吉林市昌邑区天江小区4号楼14号网点</postAddress>
		<postCode>000000</postCode>
		<sex />
		<taxPayerNum>91220201759332094N</taxPayerNum>
	</proposalAppliInfo>
	<proposalInsuredInfoList>
		<account />
		<age>23</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1995-03-08T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E34325060</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>刘苗苗</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6353</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>47</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1971-01-14T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E83496419</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>于崇森</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6354</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>38</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1980-05-01T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E83496420</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>刘术秘</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6355</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>45</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1972-12-06T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED3984471</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>李淑东</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6356</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>48</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1969-08-11T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED3984469</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>杨晓峰</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6357</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>47</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1970-11-21T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E83494039</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>孙辉</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6358</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>47</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1970-11-01T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED3983602</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>段学云</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6359</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>37</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1981-07-15T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E32741120</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>齐日光</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6360</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>37</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1981-06-13T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E83496666</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>卢海英</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6361</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>49</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1969-02-05T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E83493561</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>唐宝志</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6362</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>38</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1980-02-29T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED3966513</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>丁焕斌</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6363</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>37</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1981-03-02T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>EA8406385</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>井春</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6364</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>13</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>2004-11-03T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED3989952</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>井麒竣</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6365</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>27</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1991-03-28T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED8597664</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>周誉博</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6366</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>27</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1991-03-19T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E67345845</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>邹运</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6367</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>40</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1978-06-08T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E83492772</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>刘军</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6368</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>44</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1973-08-29T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>EB1181837</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>李金成</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6369</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>55</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1963-07-07T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED3966548</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>高荣先</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6370</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>37</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1980-11-07T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E83511147</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>杨德峰</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6371</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>52</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1965-10-04T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>EA3268273</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>李秀梅</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6372</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>25</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1992-12-08T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED3938647</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>郭超</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6373</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>26</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1992-07-18T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E19789664</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>李金书</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6374</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>32</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1986-07-17T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED8596469</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>王兆杨</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>6375</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<requestInfo>
		<password>zYjv9SSB</password>
		<transcationCode>FH180810103659508481</transcationCode>
		<user>jiangtai</user>
	</requestInfo>
	<riskCode>2711</riskCode>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<riskInfoList>
		<amount>0</amount>
		<compensateFlag />
		<kindCode />
		<netPremium>0</netPremium>
		<premium>0</premium>
		<standPremium>0</standPremium>
		<taxFee>0</taxFee>
		<taxRate>0</taxRate>
	</riskInfoList>
	<startDate>2018-08-12T12:00:00</startDate>
	<sumAmount>31827400</sumAmount>
	<sumPremium>518.94</sumPremium>
	<sumQuantity>23</sumQuantity>
	<travelInfo>
		<destinationArea>韩国</destinationArea>
		<destinationCountry>KOR</destinationCountry>
		<guideEmail />
		<guideName />
		<guidePhone />
		<leaveTime>2018-08-12T00:00:00</leaveTime>
		<trafficNumber>*</trafficNumber>
		<travelNO>SHJ18-0812济州五日游刘军二十三人</travelNO>
	</travelInfo>
</root>
"""

root =ET.XML(xml_str)

start_time = time.strptime(root.find('startDate').text, '%Y-%m-%dT%H:%M:%S')
end_time = time.strptime(root.find('endDate').text, '%Y-%m-%dT%H:%M:%S')
risk_code = root.find('riskCode').text
plan_code = root.find('planCode').text
product_code = plan_code[:-2]
order_id = root.find('orderId').text
agent_code = root.find('agentCode').text
sum_amount = float(root.find('sumAmount').text)
sum_premium = float(root.find('sumPremium').text)
apply_info_root = root.find('proposalAppliInfo')
insured_list = root.findall('proposalInsuredInfoList')
insured_cnt = len(insured_list)


chk_product_code = ''
chk_product_name = ''
chk_plan_code = ''
chk_plan_name = ''
chk_plan_sum_amount = 0.0

days = math.floor((time.mktime(end_time) - time.mktime(start_time)) / (60 * 60 * 24)) + 1

print("开始检查xml报文内容:")

sql = """select b.PRODUCTCODE,b.PRODUCTNAME,a.PROGRAMMECODE,a.PROGRAMMENAME,a.SUMAMOUNT 
from PRPDPROGRAMME a,PRPDPRODUCT b 
where a.PROGRAMMECODE='{0}'
and a.PRODUCTCODE = b.PRODUCTCODE""".format(plan_code)

row = hicis.find_one(sql)


print("3.保费检查：输入：", sum_premium)
chk_sum_premium = 0.0
insured_idx = 1
for insured in insured_list:
    sql = """select SUM(PREMIUM) from prpdratedate
where PLANCODE='{0}'
and TERMMINVALUE <= {1} AND TERMMAXVALUE >={1}
and AGEMINVALUE <= {2} AND AGEMAXVALUE>={2}
    """.format('27110024',  days,int(insured.find('age').text))
    row = hicis.find_one(sql)
    chk_sum_premium += row[0]
    print('\t\t {3:3d} 姓名：{0:5s} 年龄：{1:^3d} 保费：{2}  天数:{4}'.format(insured.find('insuredName').text, int(insured.find('age').text),row[0],insured_idx,days))
    insured_idx +=1
if round(chk_sum_premium,2) == sum_premium :
    print('\tV 检查结果：', '符合', sum_premium)
else:
    print('\tX 检查结果：', '不符合','合计人数：',insured_cnt, ' 输入：',sum_premium,'方案：',round(chk_sum_premium,2))



# sql = 'SELECT * FROM prpcmain where rownum<10'
# row = hicis.find_one(sql)

# print(row)

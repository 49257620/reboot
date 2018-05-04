# encoding: utf-8
# Author: LW


from xml.etree import ElementTree as ET
import time
import math
import dbmanager as hicis

xml_str = """<root>
<policyType>2</policyType>
<policySort>0</policySort>
<agentCode>M00000000008</agentCode>
<operateDate>2018-04-26 21:17:30</operateDate>
<startDate>2018-04-29 00:00:00</startDate>
<endDate>2018-05-04 23:59:59</endDate>
<planCode>P272017JTJJ000604</planCode>
<sumAmount>7830000.0</sumAmount>
<sumPremium>78.4</sumPremium>
<classCode>27</classCode>
<riskCode>2712</riskCode>
<businessNature>k</businessNature>
<autoTransRenewFlag>3</autoTransRenewFlag>
<arbitBoardName>北京市仲裁委员会</arbitBoardName>
<sumQuantity>0</sumQuantity>
<proposalAppliInfo><insuredName>山西东方国际旅行社有限公司</insuredName>
<identifyType>99</identifyType>
<identifyNumber>9114010070113479X7</identifyNumber>
<postAddress>/</postAddress>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredNature>4</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<birthDate>2018-04-26 21:17:29</birthDate>
<sex></sex>
<phoneNumber>17801089680</phoneNumber>
<mobile>17801089680</mobile>
<email>service@youngmanager.cn</email>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName></linkerName>
<nationalityCode>CHN</nationalityCode>
<invoicetype></invoicetype>
<taxPayerNum></taxPayerNum>
</proposalAppliInfo><proposalInsuredInfoList><insuredName>魏海燕</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142401196402230027</identifyNumber>
<birthDate>1964-02-23 00:00:00</birthDate>
<age>54</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>王永秀</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332197103160042</identifyNumber>
<birthDate>1971-03-16 00:00:00</birthDate>
<age>47</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>杨春连</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332197504152422</identifyNumber>
<birthDate>1975-04-15 00:00:00</birthDate>
<age>43</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>张晋生</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142401196503160013</identifyNumber>
<birthDate>1965-03-16 00:00:00</birthDate>
<age>53</age>
<sex>1</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>强瑞红</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142327198806210767</identifyNumber>
<birthDate>1988-06-21 00:00:00</birthDate>
<age>29</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>贺世明</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332197806054019</identifyNumber>
<birthDate>1978-06-05 00:00:00</birthDate>
<age>39</age>
<sex>1</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>刘艳梅</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332197505080029</identifyNumber>
<birthDate>1975-05-08 00:00:00</birthDate>
<age>42</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>于锦江</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142327197201290210</identifyNumber>
<birthDate>1972-01-29 00:00:00</birthDate>
<age>46</age>
<sex>1</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>王玉兰</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332197001241028</identifyNumber>
<birthDate>1970-01-24 00:00:00</birthDate>
<age>48</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>付海珍</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332196412180026</identifyNumber>
<birthDate>1964-12-18 00:00:00</birthDate>
<age>53</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>任云祯</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332197908280041</identifyNumber>
<birthDate>1979-08-28 00:00:00</birthDate>
<age>38</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>任鼠年</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332194812050010</identifyNumber>
<birthDate>1948-12-05 00:00:00</birthDate>
<age>69</age>
<sex>1</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>张小艳</insuredName>
<identifyType>01</identifyType>
<identifyNumber>141129198007190043</identifyNumber>
<birthDate>1980-07-19 00:00:00</birthDate>
<age>37</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>刘亚平</insuredName>
<identifyType>01</identifyType>
<identifyNumber>14233219710901242X</identifyNumber>
<birthDate>1971-09-01 00:00:00</birthDate>
<age>46</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>任青娥</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332197309120046</identifyNumber>
<birthDate>1973-09-12 00:00:00</birthDate>
<age>44</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>任艳红</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332198605212425</identifyNumber>
<birthDate>1986-05-21 00:00:00</birthDate>
<age>31</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>张改连</insuredName>
<identifyType>01</identifyType>
<identifyNumber>141124198510220041</identifyNumber>
<birthDate>1985-10-22 00:00:00</birthDate>
<age>32</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>王琴</insuredName>
<identifyType>01</identifyType>
<identifyNumber>14233219641231002X</identifyNumber>
<birthDate>1964-12-31 00:00:00</birthDate>
<age>53</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>乔中建</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142332197211112435</identifyNumber>
<birthDate>1972-11-11 00:00:00</birthDate>
<age>45</age>
<sex>1</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>郭桂连</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142331196111030044</identifyNumber>
<birthDate>1961-11-03 00:00:00</birthDate>
<age>56</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>韩照大</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142330195506023112</identifyNumber>
<birthDate>1955-06-02 00:00:00</birthDate>
<age>62</age>
<sex>1</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>翟成梅</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142330195805043121</identifyNumber>
<birthDate>1958-05-04 00:00:00</birthDate>
<age>59</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>刘瑞娟</insuredName>
<identifyType>01</identifyType>
<identifyNumber>14112719860319016X</identifyNumber>
<birthDate>1986-03-19 00:00:00</birthDate>
<age>32</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>李翠平</insuredName>
<identifyType>01</identifyType>
<identifyNumber>141127197110190044</identifyNumber>
<birthDate>1971-10-19 00:00:00</birthDate>
<age>46</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>刘美云</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142329197212132368</identifyNumber>
<birthDate>1972-12-13 00:00:00</birthDate>
<age>45</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>王小英</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142329197004072321</identifyNumber>
<birthDate>1970-04-07 00:00:00</birthDate>
<age>48</age>
<sex>2</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><proposalInsuredInfoList><insuredName>牛志明</insuredName>
<identifyType>01</identifyType>
<identifyNumber>142329197112272312</identifyNumber>
<birthDate>1971-12-27 00:00:00</birthDate>
<age>46</age>
<sex>1</sex>
<identifyDate>2023-04-26 00:00:00</identifyDate>
<insuredFlag>1</insuredFlag>
<insuredNature>3</insuredNature>
<insuredAddress>/</insuredAddress>
<insuredIdentity>99</insuredIdentity>
<relateSerialNo>557</relateSerialNo>
<phoneNumber>13800000000</phoneNumber>
<mobile></mobile>
<email></email>
<postAddress>*</postAddress>
<postCode>110100</postCode>
<bank></bank>
<account></account>
<linkerName> </linkerName>
<nationalityCode>CHN</nationalityCode>
<benefitFlag></benefitFlag>
<benefitRate>0.0</benefitRate>
<occupationCode>*</occupationCode>
<serialNo>1</serialNo>
</proposalInsuredInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712C01-001</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712F02-003</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712F04-005</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712F06-007</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><riskInfoList><StartDate>null</StartDate>
<EndDate>null</EndDate>
<compensateFlag>1</compensateFlag>
<kindCode>2712F23-024</kindCode>
<amount>0.0</amount>
<premium>0.0</premium>
<standPremium>0.0</standPremium>
<taxFee>0.0</taxFee>
<netPremium>0.0</netPremium>
<taxRate>0.0</taxRate>
</riskInfoList><orderId>201804262112268872366224MC5k</orderId>
<planFeeInfo><serialNo>1</serialNo>
<payNo>1</payNo>
<payReason>R10</payReason>
<planDate>2018-04-26 21:17:30</planDate>
<currency>CNY</currency>
<planFee>78.40</planFee>
<delinquentFee>0.00</delinquentFee>
<planstartdate>2018-04-26 21:17:30</planstartdate>
<productType></productType>
</planFeeInfo><Profit1>0</Profit1>
<Profit1Value></Profit1Value>
<Profit2>0</Profit2>
<Profit2Value></Profit2Value>
<travelInfo><destinationCountry>KOR</destinationCountry>
<destinationArea></destinationArea>
<travelNO></travelNO>
<leaveTime>2018-06-26 21:17:30</leaveTime>
<guideName></guideName>
<guidePhone></guidePhone>
<guideEmail></guideEmail>
<trafficNumber>---</trafficNumber>
</travelInfo><requestInfo><user>jiangtai</user>
<password>zYjv9SSB</password>
<transcationCode>201804262112268872366224MC5k888</transcationCode>
</requestInfo><productCode></productCode>
</root>
"""

root =ET.XML(xml_str)

start_time = time.strptime(root.find('startDate').text, '%Y-%m-%d %H:%M:%S')
end_time = time.strptime(root.find('endDate').text, '%Y-%m-%d %H:%M:%S')
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

if row:
    chk_product_code = row[0]
    chk_product_name = row[1]
    chk_plan_code = row[2]
    chk_plan_name = row[3]
    chk_plan_sum_amount = row[4]
    print("1.方案代码：输入：", plan_code)
    print('\tV 产品代码：', chk_product_code, '\n\tV 产品名称：', chk_product_name, '\n\tV 方案代码：', chk_plan_code, '\n\tV 方案名称：',
          chk_plan_name,
          '\n\tV 单人保额：', chk_plan_sum_amount)

    print("2.保额检查：输入：", sum_amount)

    if sum_amount == chk_plan_sum_amount * insured_cnt:
        print('\tV 检查结果：', '符合', chk_plan_sum_amount, '*', insured_cnt,
              '=', sum_amount)
    else:
        print('\tX 检查结果：', '不符合', chk_plan_sum_amount, '*', insured_cnt,
              '=', chk_plan_sum_amount * insured_cnt)

    print("3.保费检查：输入：", sum_premium)
    chk_sum_premium = 0.0
    insured_idx = 1
    for insured in insured_list:
        sql = """select SUM(PREMIUM) from prpdratedate
where PLANCODE='{0}'
and TERMMINVALUE <= {1} AND TERMMAXVALUE >={1}
and AGEMINVALUE <= {2} AND AGEMAXVALUE>={2}
        """.format(plan_code,  days,int(insured.find('age').text))
        row = hicis.find_one(sql)
        chk_sum_premium += row[0]
        print('\t\t {3:3d} 姓名：{0:5s} 年龄：{1:^3d} 保费：{2}'.format(insured.find('insuredName').text, int(insured.find('age').text),row[0],insured_idx))
        insured_idx +=1
    if round(chk_sum_premium,2) == sum_premium :
        print('\tV 检查结果：', '符合', sum_premium)
    else:
        print('\tX 检查结果：', '不符合','合计人数：',insured_cnt, ' 输入：',sum_premium,'方案：',round(chk_sum_premium,2))


else:
    print("方案不存在")


# sql = 'SELECT * FROM prpcmain where rownum<10'
# row = hicis.find_one(sql)

# print(row)

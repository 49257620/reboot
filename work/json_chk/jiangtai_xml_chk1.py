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
	<endDate>2018-06-15T23:59:59</endDate>
	<operateDate>2018-06-10T13:43:54.68</operateDate>
	<orderId>FH180610134023518923</orderId>
	<planCode>2711002</planCode>
	<planFeeInfo>
		<currency>CNY</currency>
		<delinquentFee>676.8800</delinquentFee>
		<payNo>1</payNo>
		<payReason>R10</payReason>
		<planFee>676.8800</planFee>
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
		<identifyNumber>911307023360900627</identifyNumber>
		<identifyType>99</identifyType>
		<insuredAddress>河北省张家口市桥东区工业街新天都酒店底商（市粮食局对面）</insuredAddress>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>张家口市国际旅行社</insuredName>
		<insuredNature>4</insuredNature>
		<invoicetype />
		<linkerName>李婷</linkerName>
		<mobile>13833321560</mobile>
		<nationalityCode>CHN</nationalityCode>
		<phoneNumber>13833321560</phoneNumber>
		<postAddress>河北省张家口市桥东区工业街新天都酒店底商（市粮食局对面）</postAddress>
		<postCode>000000</postCode>
		<sex />
		<taxPayerNum>911307023360900627</taxPayerNum>
	</proposalAppliInfo>
	<proposalInsuredInfoList>
		<account />
		<age>64</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1954-04-06T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>EB4420290</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>王建忠</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5858</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>63</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1954-08-29T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>EB4424326</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>高秀梅</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5859</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>67</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1951-05-06T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>EB5987268</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>李盛</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5860</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>60</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1957-12-26T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>EB5984340</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>张润来</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5861</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>55</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1962-10-27T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>EC1856723</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>刘国斌</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5862</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>55</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1963-03-30T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>EC3063125</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>胡树清</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5863</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>64</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1954-05-22T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0882554</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>张儒生</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5864</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>59</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1959-02-18T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0885196</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>梁桂平</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5865</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>56</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1961-10-30T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0885195</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>刘丽艳</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5866</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>58</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1960-04-28T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0888335</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>李秀平</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5867</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>59</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1959-03-27T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0888336</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>刘佃斌</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5868</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>59</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1959-03-26T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0885181</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>倪雅均</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5869</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>61</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1956-08-06T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0882600</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>张建</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5870</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>51</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1966-10-11T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED1931733</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>张宝莲</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5871</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>52</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1966-04-07T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED1931732</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>孙建敏</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5872</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>55</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1963-04-06T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0888333</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>杨改珍</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5873</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>69</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1949-06-09T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0882129</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>郭亮</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5874</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>59</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1958-07-03T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0888334</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>周增君</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5875</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>62</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1956-01-30T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0885182</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>温熙瑞</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5876</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>52</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1965-06-18T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED1936064</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>李丽华</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5877</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>72</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1945-10-25T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED1954685</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>周万银</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5878</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>55</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1962-07-24T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E66109316</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>赵金花</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5879</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>52</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1965-08-27T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E63066897</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>张学英</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5880</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>64</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1953-07-24T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED1954682</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>高惠荣</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5881</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>61</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1956-12-20T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0888659</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>高喜英</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5882</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>76</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1942-01-27T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>ED0888660</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>李玉衡</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5883</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>1</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>65</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1952-10-04T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E64071081</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>柳晓娟</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5884</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<proposalInsuredInfoList>
		<account />
		<age>29</age>
		<bank />
		<benefitFlag />
		<benefitRate>0</benefitRate>
		<birthDate>1988-11-02T00:00:00</birthDate>
		<email>*</email>
		<identifyNumber>E91429757</identifyNumber>
		<identifyType>03</identifyType>
		<insuredAddress>中国</insuredAddress>
		<insuredFlag>1</insuredFlag>
		<insuredIdentity>99</insuredIdentity>
		<insuredName>韩梅</insuredName>
		<insuredNature>3</insuredNature>
		<linkerName />
		<mobile />
		<nationalityCode>CHN</nationalityCode>
		<occupationCode>*</occupationCode>
		<phoneNumber>*</phoneNumber>
		<postAddress />
		<postCode>000000</postCode>
		<relateSerialNo>5885</relateSerialNo>
		<serialNo>1</serialNo>
		<sex>0</sex>
	</proposalInsuredInfoList>
	<requestInfo>
		<password>zYjv9SSB</password>
		<transcationCode>FH180610134023518923</transcationCode>
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
	<startDate>2018-06-11T12:00:00</startDate>
	<sumAmount>38746400</sumAmount>
	<sumPremium>676.88</sumPremium>
	<sumQuantity>28</sumQuantity>
	<travelInfo>
		<destinationArea>韩国</destinationArea>
		<destinationCountry>KOR</destinationCountry>
		<guideEmail />
		<guideName />
		<guidePhone />
		<leaveTime>2018-06-11T00:00:00</leaveTime>
		<trafficNumber>*</trafficNumber>
		<travelNO>2018.06.11</travelNO>
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

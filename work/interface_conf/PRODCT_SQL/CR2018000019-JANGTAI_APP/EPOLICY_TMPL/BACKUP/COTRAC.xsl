<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:lxslt="http://xml.apache.org/xslt" xmlns:result="http://www.example.com/results" extension-element-prefixes="result" version="1.0" xmlns:java="com.indigo.software.idp.agent" exclude-result-prefixes="java">
	<xsl:template match="/">
		<PACKET>
			<!--头信息 与处理流程有关-->
			<HEAD>
				<!--请求类型代码(E01:保单生成，E02:保单下载，E03：保单验真)-->
				<KEY><xsl:value-of select="PACKET/HEAD/KEY"/></KEY>
				<!--唯一单证号（保单就是保单号） -->
				<NUM><xsl:value-of select="PACKET/HEAD/NUM"/></NUM>
				<!-- 单证类型  A保单 B批单-->
				<TYPE><xsl:value-of select="PACKET/HEAD/TYPE"/></TYPE>
				<!--险种代码-->
				<E_CODE><xsl:value-of select="PACKET/HEAD/E_CODE"/></E_CODE>
			</HEAD>
			<!--主结点信息（与模板中展示内容无关）-->
			<MAIN>
				<!--交易时间 核心请求接口时的时间格式：YYYY-MM-DD HH24:MI:SS -->
				<TRADE_TIME><xsl:value-of select="PACKET/MAIN/TRADE_TIME"/></TRADE_TIME>
				<!--单证模板代码 -->
				<POLICY_TYPE><xsl:value-of select="PACKET/MAIN/POLICY_TYPE"/></POLICY_TYPE>
				<!--投保人名称 -->
				<APPLICANT_NAME><xsl:value-of select="PACKET/MAIN/APPLICANT_NAME"/></APPLICANT_NAME>
				<!-- 证件类型-->
				<CREDENTIAL_TYPE><xsl:value-of select="PACKET/MAIN/CREDENTIAL_TYPE"/></CREDENTIAL_TYPE>
				<!--客户证件号 -->
				<CREDENTIAL_NO><xsl:value-of select="PACKET/MAIN/CREDENTIAL_NO"/></CREDENTIAL_NO>
				<!--客户手机号 -->
				<PHONE_NO><xsl:value-of select="PACKET/MAIN/PHONE_NO"/></PHONE_NO>
				<!-- 客户邮箱-->
				<E_MAIL><xsl:value-of select="PACKET/MAIN/E_MAIL"/></E_MAIL>
				<!--是否发邮件 1：发送 0 不发送-->
				<IF_EMAIL><xsl:value-of select="PACKET/MAIN/IF_EMAIL"/></IF_EMAIL>
				<!--签名算法 默认传送SM2-->
				<SIGN><xsl:value-of select="PACKET/MAIN/SIGN"/></SIGN>
				<!--邮件内容-->
				<EMAIL_MSG><xsl:value-of select="PACKET/MAIN/EMAIL_MSG"/></EMAIL_MSG>
				<!--邮件标题-->
				<EMAIL_HEAD><xsl:value-of select="PACKET/MAIN/EMAIL_HEAD"/></EMAIL_HEAD>
				<!--短信内容-->
				<SHORT_MSG><xsl:value-of select="PACKET/MAIN/SHORT_MSG"/></SHORT_MSG>
				<!--分公司代码-->
				<BRANCH_CODE><xsl:value-of select="PACKET/MAIN/BRANCH_CODE"/></BRANCH_CODE>
				<!--条款代码-->
				<xsl:choose>
					<xsl:when test="PACKET/MAIN/Clauses/Clause/name!=''">
						<Clauses>
							<xsl:for-each select="PACKET/MAIN/Clauses/Clause">
								<Clause>
									<name>
										<xsl:value-of select="name"/>
									</name>
								</Clause>
							</xsl:for-each>
						</Clauses>
					</xsl:when>
					<xsl:otherwise>
						<clausenull>
							<name/>
						</clausenull>
					</xsl:otherwise>
				</xsl:choose>
			</MAIN>
			<!--基本信息 （需要在模板中展示的内容）-->
			<BASE_INFO>
				<!--保单号-->
				<V1><xsl:value-of select="PACKET/BASE_INFO/V1"/></V1>
				<!--投保人姓名-->
				<V2><xsl:value-of select="PACKET/BASE_INFO/V2"/></V2>
				<!--投保人电话-->
				<V3><xsl:value-of select="PACKET/BASE_INFO/V3"/></V3>
				<!--投保人邮箱-->
				<V4><xsl:value-of select="PACKET/BASE_INFO/V4"/></V4>
				<!--投保人地址-->
				<V5><xsl:value-of select="PACKET/BASE_INFO/V5"/></V5>
				<!--投保人邮编-->
				<V6><xsl:value-of select="PACKET/BASE_INFO/V6"/></V6>
				<!--
				<V7><xsl:value-of select="PACKET/BASE_INFO/V7"/></V7>
				-->
				<!--受益人-->
				<xsl:choose>
					<xsl:when test="PACKET/BASE_INFO/V7!=''">
						<V7><xsl:value-of select="PACKET/BASE_INFO/V7"/></V7>
					</xsl:when>
					<xsl:otherwise>
						<V7>法定</V7>
					</xsl:otherwise>
				</xsl:choose>
				<!--电子保单标题-->
				<V8><xsl:value-of select="PACKET/BASE_INFO/V8"/></V8>
				<!--保险天数-->
				<V9><xsl:value-of select="PACKET/BASE_INFO/V9"/></V9>
				<!--旅游目的地-->
				<!--<V10><xsl:value-of select="PACKET/BASE_INFO/V10"/></V10>-->
				<xsl:choose>
					<xsl:when test="PACKET/BASE_INFO/V10!=''">
						<V10><xsl:value-of select="PACKET/BASE_INFO/V10"/></V10>
					</xsl:when>
				</xsl:choose>
				<!--起保时间-->
				<V11><xsl:value-of select="PACKET/BASE_INFO/V11"/></V11>
				<!--起保小时-->
				<V12><xsl:value-of select="PACKET/BASE_INFO/V12"/></V12>
				<!--终保时间-->
				<V13><xsl:value-of select="PACKET/BASE_INFO/V13"/></V13>
				<!--终保小时-->
				<V14><xsl:value-of select="PACKET/BASE_INFO/V14"/></V14>
				<!--每人保费-->
				<!--<V15>CNY <xsl:value-of select="PACKET/BASE_INFO/V15"/></V15>-->
				<!--合计保费-->
				<!--<V16>CNY <xsl:value-of select="PACKET/BASE_INFO/V16"/></V16>-->
				
				<xsl:variable name="V15" select="/PACKET/BASE_INFO/V15"/>
				<V15>CNY <xsl:value-of select='format-number($V15,"###,###.00")'/></V15>
				<xsl:variable name="V16" select="/PACKET/BASE_INFO/V16"/>
				<V16>CNY <xsl:value-of select='format-number($V16,"###,###.00")'/></V16>
				
			
        <!--V17-V29 数据库备用字段-->
				<V17><xsl:value-of select="PACKET/BASE_INFO/V17"/></V17>
				<V18><xsl:value-of select="PACKET/BASE_INFO/V18"/></V18>
				<V19><xsl:value-of select="PACKET/BASE_INFO/V19"/></V19>
				<V20><xsl:value-of select="PACKET/BASE_INFO/V20"/></V20>
				<V21><xsl:value-of select="PACKET/BASE_INFO/V21"/></V21>
				<V22><xsl:value-of select="PACKET/BASE_INFO/V22"/></V22>
				<V23><xsl:value-of select="PACKET/BASE_INFO/V23"/></V23>
				<V24><xsl:value-of select="PACKET/BASE_INFO/V24"/></V24>
				<V25><xsl:value-of select="PACKET/BASE_INFO/V25"/></V25>
				<V26><xsl:value-of select="PACKET/BASE_INFO/V26"/></V26>
				<V27><xsl:value-of select="PACKET/BASE_INFO/V27"/></V27>
				<V28><xsl:value-of select="PACKET/BASE_INFO/V28"/></V28>
				<V29><xsl:value-of select="PACKET/BASE_INFO/V29"/></V29>
				<!--救援电话-->
				<V30><xsl:value-of select="PACKET/BASE_INFO/V30"/></V30>
				<!--V31-V44 程序备用字段-->
				<V31><xsl:value-of select="PACKET/BASE_INFO/V31"/></V31>
				<V32><xsl:value-of select="PACKET/BASE_INFO/V32"/></V32>
				<V33><xsl:value-of select="PACKET/BASE_INFO/V33"/></V33>
				<V34><xsl:value-of select="PACKET/BASE_INFO/V34"/></V34>
				<V35><xsl:value-of select="PACKET/BASE_INFO/V35"/></V35>
				<V36><xsl:value-of select="PACKET/BASE_INFO/V36"/></V36>
				<V37><xsl:value-of select="PACKET/BASE_INFO/V37"/></V37>
				<V38><xsl:value-of select="PACKET/BASE_INFO/V38"/></V38>
				<V39><xsl:value-of select="PACKET/BASE_INFO/V39"/></V39>
				<V40><xsl:value-of select="PACKET/BASE_INFO/V40"/></V40>
				<V41><xsl:value-of select="PACKET/BASE_INFO/V41"/></V41>
				<V42><xsl:value-of select="PACKET/BASE_INFO/V42"/></V42>
				<V43><xsl:value-of select="PACKET/BASE_INFO/V43"/></V43>
				<V44><xsl:value-of select="PACKET/BASE_INFO/V44"/></V44>
				<!--出单日期-->
				<V45><xsl:value-of select="PACKET/BASE_INFO/V45"/></V45>
				<!--特别约定-->
				<V46><xsl:value-of select="PACKET/BASE_INFO/V46"/></V46>
				<!--公司名称-->
				<V47><xsl:value-of select="PACKET/BASE_INFO/V47"/></V47>
				<!--公司地址-->
				<V48><xsl:value-of select="PACKET/BASE_INFO/V48"/></V48>
				<!--联系电话-->
				<V49><xsl:value-of select="PACKET/BASE_INFO/V49"/></V49>
				<!--网站地址-->
				<V50><xsl:value-of select="PACKET/BASE_INFO/V50"/></V50>
				<!--V51 参数转化为保险期限字符串-->
				<V51>自<xsl:value-of select="PACKET/BASE_INFO/V11"/><xsl:value-of select="PACKET/BASE_INFO/V12"/>时起，至<xsl:value-of select="PACKET/BASE_INFO/V13"/><xsl:value-of select="PACKET/BASE_INFO/V14"/>时止 共计<xsl:value-of select="PACKET/BASE_INFO/V9"/>天（北京时间）</V51>
				<!--R1 被保险人信息-->
				<R1>
					<Row>					
						<xsl:choose>
							<xsl:when test="PACKET/BASE_INFO/R1/Row/RV1='1'">
								<!--被保险人数-->
								<RV1><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV1"/>人</RV1>
								<!--被保险人姓名-->
								<RV2><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV2"/></RV2>
								<!--证件类型-->
								<RV3><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV3"/></RV3>
								<!--证件号-->
								<RV4><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV4"/></RV4>
								<!--性别-->
								<RV5><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV5"/></RV5>
								<!--生日-->
								<RV6><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV6"/></RV6>
								<!--年龄-->
								<RV7><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV7"/></RV7>
								<RV8><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV8"/></RV8>
								<RV9><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV9"/></RV9>
								<RV10><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV10"/></RV10>
							</xsl:when>
							<xsl:otherwise>
								<RV1><xsl:value-of select="PACKET/BASE_INFO/R1/Row/RV1"/>人，详见清单</RV1>
								<RV2>详见清单</RV2>
								<RV3>详见清单</RV3>
								<RV4>详见清单</RV4>
								<RV5>详见清单</RV5>
								<RV6>详见清单</RV6>
								<RV7>详见清单</RV7>
								<RV8></RV8>
								<RV9></RV9>
								<RV10></RV10>
							</xsl:otherwise>
						</xsl:choose>
					</Row>
				</R1>
				<!--R2 保障项目-->				
				<R2>
					<xsl:for-each select="PACKET/BASE_INFO/R2/Row">
						<Row>		
							<!--保障项目代码-->			
							<RV1><xsl:value-of select="RV1"/></RV1>
							<!--保障项目名称-->		
							<RV2><xsl:value-of select="RV2"/></RV2>
							<!--保障项目kindname-->		
							<RV3><xsl:value-of select="RV3"/></RV3>		
							<!--保障项目代码-->							
							<!--<RV4><xsl:value-of select="RV4"/></RV4>-->			
							<!--总保额-->		
							<!--<RV5>CNY <xsl:value-of select="RV5"/></RV5>-->			
							<!--单人保额-->		
							<!--<RV6>CNY <xsl:value-of select="RV6"/></RV6>-->			
							<!--总保费-->		
							<!--<RV7>CNY <xsl:value-of select="RV7"/></RV7>-->			
							<!--单人保费-->		
							<RV8>CNY <xsl:value-of select="RV8"/></RV8>
							<!--主险1附加险2-->		
							<RV9><xsl:value-of select="RV9"/></RV9>
							<RV10><xsl:value-of select="RV10"/></RV10>
							
							<xsl:variable name="RV4" select="RV4"/>
							<RV4>CNY <xsl:value-of select='format-number($RV4,"###,###.00")'/></RV4>			
							<xsl:variable name="RV5" select="RV5"/>
							<RV5>CNY <xsl:value-of select='format-number($RV5,"###,###.00")'/></RV5>
							<xsl:variable name="RV6" select="RV6"/>
							<RV6>CNY <xsl:value-of select='format-number($RV6,"###,###.00")'/></RV6>			
							<xsl:variable name="RV7" select="RV7"/>
							<RV7>CNY <xsl:value-of select='format-number($RV7,"###,###.00")'/></RV7>
							
							
						</Row>
					</xsl:for-each>
				</R2>
				
				<xsl:choose>
					<xsl:when test="PACKET/BASE_INFO/R1/Row/RV1='1'">					
					</xsl:when>
					<xsl:otherwise>
						<!--R3 被保险人清单-->		
						<R3>
							<xsl:for-each select="PACKET/BASE_INFO/R3/Row">
								<Row>
									<!--序号-->		
									<RV1><xsl:value-of select="RV1"/></RV1>
									<!--被保险人姓名-->	
									<RV2><xsl:value-of select="RV2"/></RV2>
									<!--证件类型-->
									<RV3><xsl:value-of select="RV3"/></RV3>
									<!--证件号-->
									<RV4><xsl:value-of select="RV4"/></RV4>	
									<!--性别-->								
									<RV5><xsl:value-of select="RV5"/></RV5>
									<!--生日-->
									<RV6><xsl:value-of select="RV6"/></RV6>
									<!--年龄-->
									<RV7><xsl:value-of select="RV7"/></RV7>
									<!--保额-->		
									<RV8>CNY <xsl:value-of select="RV8"/></RV8>
									<!--保费-->		
									<!--<RV9>CNY <xsl:value-of select="RV9"/></RV9>-->
									<xsl:variable name="RV9" select="RV9"/>
									<RV9>CNY <xsl:value-of select='format-number($RV9,"###,###.00")'/></RV9>		
									<RV10><xsl:value-of select="RV10"/></RV10>
									
								</Row>
							</xsl:for-each>
						</R3>
					</xsl:otherwise>
				</xsl:choose>
			</BASE_INFO>
		</PACKET>
	</xsl:template>
</xsl:stylesheet>

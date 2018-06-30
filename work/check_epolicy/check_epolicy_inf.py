# encoding: utf-8
# Author: LW

from suds.client import Client

WSDL_URL_OP = 'https://channel.hi-ins.com.cn/wsservice/ElectronicpolicyService?wsdl'
WSDL_URL = 'http://122.200.121.148/wsservice/ElectronicpolicyService?wsdl'
URL_OP = 'https://channel.hi-ins.com.cn/wsservice/ElectronicpolicyService'
URL = 'http://122.200.121.148/wsservice/ElectronicpolicyService'

downLoad = {}
downLoad['key'] = 'E02'
downLoad['num'] = '827122018110100000377'
downLoad['type'] = 'A'
downLoad['requestInfo'] = {'password': 'baichuan', 'user': 'baichuan', 'transcationCode': 'BCJJ-xiandai2018sbsbsbsbs'}
client = Client(WSDL_URL)
result = client.service.downPdf(downLoad, location=URL)

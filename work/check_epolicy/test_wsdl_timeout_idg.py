# encoding: utf-8
# Author: LW

WSDL_URL = 'http://10.69.10.115:8081/axis/services/IDGWS'  # 测试

def run_webservice(proposal_date):
    from suds import WebFault
    from suds.client import Client
    client = Client(WSDL_URL)
    print(client)

    result = client.service.submitJob("")

    print(result)





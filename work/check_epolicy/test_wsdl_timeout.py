# encoding: utf-8
# Author: LW

WSDL_URL = 'http://10.69.80.20:2001/prpall/services/ProfessionalServiceimplJN?wsdl'  # 测试

def run_webservice(proposal_date):
    from suds import WebFault
    from suds.client import Client
    client = Client(WSDL_URL)
    # print(client)

    policyInfo = {}
    policyInfo['agentCode'] = proposal_date[1]
    policyInfo['proposalNo'] = proposal_date[0]
    policyInfo['requestInfo'] = {'password': 'c64fe1a8', 'user': 'jiangtai',
                                 'transcationCode': 'JTJJ-xiandai2018sbsbsbsbs'}
    result = client.service.proposalConfirm(policyInfo)
    return result


for x in range(10):
    print(run_webservice('927012018110100000288','M00000000008'))
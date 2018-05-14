# encoding: utf-8
# Author: LW

import dbmanager_mysql as mysql_conn
import dbmanager_oracle as oracle_conn
import time

# WSDL_URL = 'http://10.69.80.20:2001/prpall/services/ProfessionalServiceimplJN?wsdl'  # 测试
WSDL_URL = 'http://10.69.17.35:80/wsservice/ProfessionalServiceimplJN?wsdl'  # 生产

SLEEP_TIME = 5  # 休眠时间 单位：分钟


def get_dif_policy_no():
    sql_idg = "select BUSSNO from TB_PROCESSQUEUE where CREATETIME > DATE_SUB(CURDATE(),INTERVAL 0 DAY)"

    idg_data = mysql_conn.find_all(sql_idg)

    idg_set = set()

    for x in idg_data:
        idg_set.add(x[0])

    print('\t IDG 数量：', len(idg_set), end='')

    sql_hic = "select BUSINESSNO from Prpepolicystate where state='3' and (BUSINESSNO like '827%' or BUSINESSNO like '829%') and  TRADEDATE LIKE '2018%'  AND  to_date(TRADEDATE,'YYYY-MM-DD HH24-MI-SS') >= TO_DATE(TO_CHAR(SYSDATE,'YYYYMMDD')||'000000','YYYYMMDDHH24MISS') AND to_date(TRADEDATE,'YYYY-MM-DD HH24-MI-SS') < (SYSDATE-10/24/60) "

    hic_data = oracle_conn.find_all(sql_hic)

    hic_set = set()
    for x in hic_data:
        hic_set.add(x[0])

    print('  HIC 数量：', len(hic_set))

    new_set = hic_set - idg_set
    return new_set


def run_webservice(proposal_date):
    from suds import WebFault
    from suds.client import Client
    client = Client(WSDL_URL)
    # print(client)

    policyInfo = {}
    policyInfo['agentCode'] = proposal_date[1]
    policyInfo['proposalNo'] = proposal_date[0]
    policyInfo['requestInfo'] = {'password': 'zYjv9SSB', 'user': 'jiangtai',
                                 'transcationCode': 'JTJJ-xiandai2018sbsbsbsbs'}
    result = client.service.proposalConfirm(policyInfo)
    return result['responseInfo']


"""
(policyResponseInfo){
   policyNo = "827012018110100000131"
   responseInfo = 
      (responseInfo){
         errorCode = "0000"
         errorMessage = "成功"
         responseCode = "1"
      }
 }
"""


def get_proposal_no(policy_no):
    sql_proposal = "select PROPOSALNO,agentcode from prpcmain where policyno ='{0}' ".format(policy_no)

    proposal_date = oracle_conn.find_one(sql_proposal)

    if proposal_date:
        return proposal_date
    else:
        return None


# print(get_proposal_no('827122018110100000793'))


def start_que(sleep_time):
    print('开始检查江泰电子保单生成情况，每{0}分钟检查一次，\n处理一个保单后休眠1分钟，然后继续处理。\n23:30 - 00:30 不做处理。'.format(SLEEP_TIME))
    idx = 1
    while True:
        c_time = time.localtime(time.time())
        if c_time[3] == 23 and c_time[4] > 30 :
            print('进入休眠时间，休眠60分钟')
            time.sleep(60*60)
            continue
        print('第 {0} 次请求：请求时间：{1}'.format(idx, time.asctime(time.localtime(time.time()))))
        to_do_list = get_dif_policy_no()
        if len(to_do_list) > 0:
            print('\t 共计 {} 件保单需生成！'.format(len(to_do_list)))
            run_idx = 1
            for x in to_do_list:
                proposal_date = get_proposal_no(x)
                if proposal_date:
                    result = run_webservice(proposal_date)
                    if result['errorCode'] == '0000':
                        print('\t {2} {0} {1} 执行成功！'.format(x, proposal_date[0], run_idx))
                    else:
                        print('\t {2} {0} {1} 执行失败！'.format(x, proposal_date[0], run_idx))
                    time.sleep(60)
                else:
                    print('\t {1} {0} 未找到投保单号！'.format(x, run_idx))
                run_idx += 1
        else:
            print('\t 没有需生成的保单!')
        idx += 1
        time.sleep(sleep_time)


if __name__ == "__main__":
    start_que(60*SLEEP_TIME)
    # print(get_proposal_no('827122018110100000793'))
    # print(get_dif_policy_no())
    # print(run_webservice(('927122018110100002199','M00000000008')))

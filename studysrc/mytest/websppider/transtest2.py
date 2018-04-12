# encoding: utf-8
# Author: LW

import urllib
import json
import time
import random
import hashlib
import urllib.request

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {
"Accept":" application/json, text/javascript, */*; q=0.01",
"X-Requested-With":" XMLHttpRequest",
"User-Agent":" Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"Accept-Language":" zh-CN,zh;q=0.9"

}

key ='so this'

u = 'fanyideskweb'
d = key
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'ebSeFb%=XZ%T[KZ)c(sy!'
'''
md5 = hashlib.md5()
md5.update(u.encode('utf-8'))
md5.update(d.encode('utf-8'))
md5.update(f.encode('utf-8'))
md5.update(c.encode('utf-8'))
sign = md5.hexdigest()
'''
sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

data = {
"i":key,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":f,
"sign":sign,
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTIME",
"typoResult":"false"
}



data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
# response = urllib.request.urlopen(url,data)
line = json.load(response)
print(line['translateResult'][0][0]['tgt'])
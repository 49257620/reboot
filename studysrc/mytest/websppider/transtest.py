# encoding: utf-8
# Author: LW

import urllib.request
import urllib.parse
import time
import random
import hashlib

content = 'what fuck'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data = {}
'''
1523493384696
1523493371204
351ac046404e1bbcb9442615f964a96d
cb2731255a15489013919b3788953bdc
'''
u = 'fanyideskweb'
d = content
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'ebSeFb%=XZ%T[KZ)c(sy!'


sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
print(f)
print(sign)

data['i']: content
data['from']: 'AUTO'
data['to']: 'AUTO'
data['smartresult']: 'dict'
data['client']: 'fanyideskweb'
data['salt'] = f
data['sign'] = sign
data['doctype']: 'json'
data['version']: '2.1'
data['keyfrom']: 'fanyi.web'
data['action']: 'FY_BY_CLICKBUTTION'
data['typoResult']: 'false'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)

html = response.read().decode('utf-8')

print(html)

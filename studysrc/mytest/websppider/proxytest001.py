# encoding: utf-8
# Author: LW

import urllib.request


url = 'http://icanhazip.com/'

# url = 'http://www.baidu.com'



proxy_support = urllib.request.ProxyHandler({'http':'42.104.84.107:8080'})

openner = urllib.request.build_opener(proxy_support)

#openner.addheaders([('User-Agent','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11')])
#openner.addheaders()
urllib.request.install_opener(openner)

response = urllib.request.urlopen(url)


html = response.read().decode('utf-8')

print(html)
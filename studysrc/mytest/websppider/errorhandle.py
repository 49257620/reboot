# encoding: utf-8
# Author: LW

import urllib.request
import urllib.error

req = urllib.request.Request("http://www.ooxx-liuwei.xom")
try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e)


req = urllib.request.Request("http://www.fishc.com/ooxx.html")
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e)
    print(e.code)
    print(e.info())




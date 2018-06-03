# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


import hashlib

ss_tmp = ""
md5 = hashlib.md5()
# 转成二进制字符串
md5.update(ss_tmp.encode())
ss = md5.hexdigest()

print(ss)

# hashlib.sha256()

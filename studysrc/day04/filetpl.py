# encoding: utf-8
# -*- coding: encoding -*-
# author = ‘LW’

tpl = open('filetplngx.tpl', 'rt', encoding='utf-8').read()

open('filetplngx.conf', 'wt').write(tpl.format(host='19.19.19.19', port='8080'))

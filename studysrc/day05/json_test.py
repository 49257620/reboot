# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

import json


l1 = [{'name': 'll', 'age': 30}, {'name': 'll', 'age': 21}, {'name': 'll', 'age': 19}]

print(l1)

json_str = json.dumps(l1)

print(json_str)

ll = json.loads(json_str)

print(l1)
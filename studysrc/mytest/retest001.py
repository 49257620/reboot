# encoding: utf-8
# Author: LW

import re


print(re.search(r'FishC','I love FishC.com!'))

print(re.search(r'.','I love FishC.com!'))

print(re.search(r'Fish.','I love FishC.com!'))

print(re.search(r'\.','I love FishC.com!'))

print(re.search(r'\d\d\d','I love 123 FishC.com!'))
print(re.search(r'\d\d','I love 123 FishC.com!'))

print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d','192.168.0.1'))
print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d','192.168.111.111'))

print(re.search(r'[aeiou]','I love FishC.com!'))
print(re.search(r'[aeiouAEIOU]','I love FishC.com!'))

print(re.search(r'[a-z]','I love FishC.com!'))

print(re.search(r'[0-9]','I love 123 FishC.com!'))
print(re.search(r'[2-9]','I love 123 FishC.com!'))

print(re.search(r'ab{3}c','abbbc'))

print(re.search(r'ab{3,10}c','abbbbbbbc'))

print(re.search(r'[01]\d\d|2[0-4]]\d|25[0-5]','188'))

print(re.search(r'[01]{0,1}\d{0,1}\d|2[0-4]]\d|25[0-5]','192'))

print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]]\d|25[0-5])','192.168.111.111'))
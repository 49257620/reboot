# encoding: utf-8
# Author: LW

import urllib.request

response = urllib.request.urlopen('http://placekitten.com/500/600')

print(response.getcode())
cat_img = response.read()

with open('E://cat_500_600.jpg','wb') as f:
    f.write(cat_img)


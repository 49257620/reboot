# encoding: utf-8
# author = ‘LW’

start_idx = 0

chars = 'abcabcabcabc'

while True:
    s = chars.find('ab', start_idx)
    if s == -1:
        break
    print(s)
    start_idx = s + 1

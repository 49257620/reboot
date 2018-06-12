# encoding: utf-8
# Author: LW

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        while s.find('()')!=-1 or s.find('[]')!=-1 or s.find('{}')!=-1:
            s = s.replace('()','')
            s = s.replace('[]', '')
            s = s.replace('{}', '')

        if s == '':
            return  True
        else:
            return False



a = '{[]}'
print(Solution().isValid(a))

# encoding: utf-8
# Author: LW

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip() =='':
            return 0
        else:
            str_list = s.split()
            return len(str_list[-1])




n = 'Hello World'
print(Solution().lengthOfLastWord(n))


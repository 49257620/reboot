# encoding: utf-8
# Author: LW

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0;
        for x in range(len(digits)):
            num += digits[x]*10**(len(digits)-x-1)

        ss = str(num+1)

        return [ int(x) for x in list(ss)]



n = [4,3,2,1]
print(Solution().plusOne(n))


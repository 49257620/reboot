# encoding: utf-8
# Author: LW

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        s = x_str[::-1]
        if x_str == s :
            return  True
        else:
            return False

a = -121
print(Solution().isPalindrome(a))
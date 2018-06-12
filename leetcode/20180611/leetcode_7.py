# encoding: utf-8
# Author: LW

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        [−231,  231 − 1]
        """

        if x > 0:
            nn = 1
        else:
            x = x * -1
            nn = -1
        x_str = str(x)
        s = x_str[::-1]
        result = int(s)*nn
        if result > 2**31 -1 or result < -(2**31):
            return 0
        else:
            return result

a = 1534236469
print(Solution().reverse(a))
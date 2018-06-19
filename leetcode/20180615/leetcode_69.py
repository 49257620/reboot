# encoding: utf-8
# Author: LW

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        return int(math.sqrt(x))



a = 8

print(Solution().mySqrt(a))


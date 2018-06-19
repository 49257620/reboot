# encoding: utf-8
# Author: LW

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step_cnt = 0
        if n <=3:
            return  n
        l1 = 2
        l2 = 3
        for x in range(3,n):
            step_cnt =  l1 +l2
            l1,l2 = l2 ,step_cnt

        return   step_cnt



    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <=3:
            return n
        else:
            return (n-1) +(n-2)



a = 6

print(Solution().climbStairs(a))


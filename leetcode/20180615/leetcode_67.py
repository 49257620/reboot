# encoding: utf-8
# Author: LW

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        t_a = int(a,2)
        t_b = int(b,2)

        result = t_a +t_b

        return str(bin(result))[2:]



a = "11"
b = "1"
print(Solution().addBinary(a,b))


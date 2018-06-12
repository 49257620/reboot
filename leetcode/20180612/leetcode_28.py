# encoding: utf-8
# Author: LW

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        return haystack.find(needle)



haystack = 'hello'
needle = 'll'
print(Solution().strStr(haystack,needle))

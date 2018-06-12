# encoding: utf-8
# Author: LW

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        tt = zip(*[x for x in strs])
        for x in tt:
            if len(set(x)) ==1:
                result += set(x).pop()
            else :
                break
        return result


a = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(a))

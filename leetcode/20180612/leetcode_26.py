# encoding: utf-8
# Author: LW

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_set = set(nums)
        tmp_list = list(tmp_set)
        tmp_list = sorted(tmp_list)
        for x in range(len(tmp_list)):
            nums[x] =  tmp_list[x]
        return len(tmp_list)



a = [1,1,2]
print(Solution().removeDuplicates(a))

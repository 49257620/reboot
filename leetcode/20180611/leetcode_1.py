# encoding: utf-8
# Author: LW

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return list((i,j))


a = [2,7,11,15]
b = 9

print(Solution().twoSum(a,b))
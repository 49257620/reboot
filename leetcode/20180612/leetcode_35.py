# encoding: utf-8
# Author: LW

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for x in range(len(nums)):
            if nums[x] >= target:
                return x

        return  len(nums)



nums = [1,3,5,6]
target = 5
print(Solution().searchInsert(nums,target))

# encoding: utf-8
# Author: LW

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_list = nums[:]
        while  val in tmp_list:
            tmp_list.remove(val)
        for x in range(len(tmp_list)):
            nums[x] =  tmp_list[x]

        return len(tmp_list)



nums = [0,1,2,2,3,0,4,2]
val = 2
print(Solution().removeElement(nums,val))

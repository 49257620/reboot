"""
198. 打家劫舍

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

"""


class Solution:

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        a = nums[0]
        b = max([nums[0], nums[1]])

        for x in range(2,len(nums)):
            a,b = b,max(a+nums[x],b)

        return b

    def rob5(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)

        max_num = max(nums)

        max_cnt = nums.count(max_num)


        max_index = nums.index(max_num)



        #print(max_index,nums[:max_index-1],nums[max_index+2:])
        x = max_num + self.rob4(nums[:max_index-1 if max_index-1 >=0 else 0]) + self.rob4(nums[max_index+2:])

        max_index = nums.index( max(nums))-1
        if max_index >= 0:
            max_num = nums[max_index]
            y = max_num + self.rob4(nums[:max_index - 1 if max_index - 1 >= 0 else 0]) + self.rob4(nums[max_index + 2:])
        else:
            y= -10000

        max_index = nums.index( max(nums)) + 1
        if max_index < len(nums):
            max_num = nums[max_index]
            z = max_num + self.rob4(nums[:max_index - 1 if max_index - 1 >= 0 else 0]) + self.rob4(nums[max_index + 2:])
        else:
            z = -10000
        print(x,y,z)
        return max([x,y,z])

    def rob4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)

        max_num = max(nums)
        max_index = nums.index(max_num)
        max_cnt = nums.count(max_num)
        if max_cnt == 1:
            max_index = nums.index(max_num)
        else:

            max_index = nums.index(max_num, nums.index(max_num) + 1)
        #print(max_index,nums[:max_index-1],nums[max_index+2:])
        return max_num + self.rob(nums[:max_index-1 if max_index-1 >=0 else 0]) + self.rob(nums[max_index+2:])

    def rob3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)

        max_num = max(nums)
        max_index = nums.index(max_num)
        print(max_index,nums[:max_index-1],nums[max_index+2:])
        return max_num + self.rob(nums[:max_index-1 if max_index-1 >=0 else 0]) + self.rob(nums[max_index+2:])

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return sum(nums)
        if len(nums)==2:
            return max(nums)
        lll = []
        s1= nums[0]
        s2 =nums[1]
        l1 = [nums[x] for x in range(len(nums)) if x % 2 == 0 ]
        l2 = [nums[x] for x in range(len(nums)) if x % 2 != 0 ]
        lll.append(sum(l1))
        lll.append(sum(l2))
        lll.append(sum(nums[1:2] +l1[2:]))
        lll.append(sum(nums[0:1] + l2[1:]))
        return max(lll)

    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1 = [nums[x] for x in range(len(nums)) if x%2==0]
        l2 = [nums[x] for x in range(len(nums)) if x % 2 != 0]

        #print(sum(l1))
        #print(sum(l2))

        return sum(l1) if sum(l1)>sum(l2) else sum(l2)



if __name__ == '__main__':
    ll = Solution().rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])
    print(ll)



"""
169. 求众数

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for x in nums:
            mydict[x] = mydict.get(x,0)+1

        return sorted(mydict,key=lambda x:mydict[x])[-1]


if __name__ == '__main__':
    ll = Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])

    print(ll)

"""
167. 两数之和 II - 输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

"""



class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        filterlist = list(set(numbers))  # [x for x in numbers if abs(x)<=abs(target)]
        if filterlist.count(0)==1:
            filterlist.append(0)
        if filterlist.count(target//2)==1:
            filterlist.append(target//2)
        print(filterlist)
        for x in range(len(filterlist)):
            for y in range(x + 1, len(filterlist)):
                # print(filterlist[x],filterlist[y])
                if filterlist[x] + filterlist[y] == target:
                    if filterlist[x] <= filterlist[y]:
                        return [numbers.index(filterlist[x]) + 1,
                            numbers.index(filterlist[y], numbers.index(filterlist[x]) + 1) + 1]
                    else:
                        return [numbers.index(filterlist[y]) + 1,
                                numbers.index(filterlist[x], numbers.index(filterlist[y]) + 1) + 1]
        return None


if __name__ == '__main__':
    ll = Solution().twoSum([0,0,3,4]
,0)

    print(ll)
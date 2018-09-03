"""

119. 杨辉三角 II

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
"""


class Solution:
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows ==0:
            return []
        ll = []
        for x in range(numRows+1):
            lll = []
            if x ==0:
                ll.append([1])
            elif x == 1:
                ll.append([1,1])
            else:
                lll.append(1)
                for y in range(len(ll[x-1])-1):
                    lll.append(ll[x-1][y]+ll[x-1][y+1])
                lll.append(1)
                ll.append(lll)

        return lll


if __name__ == '__main__':
    ll = Solution().getRow(3)
    print(ll)
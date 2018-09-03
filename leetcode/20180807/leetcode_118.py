"""

118. 杨辉三角

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ll = []
        for x in range(numRows):
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

        return ll


if __name__ == '__main__':
    ll = Solution().generate(5)
    print(ll)
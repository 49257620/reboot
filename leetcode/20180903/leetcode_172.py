"""
172. 阶乘后的零

给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。

"""


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int


        result = 1
        for x in range(1,n):
            result *= x

            cnt = 0;
            for y in reversed(str(result)):
                if y == '0':
                    cnt += 1
                else:
                    break

            print(x,x//5 + x//5//5,cnt,cnt-(x//5 + x//5//5))
                """
        if n ==0:
            return 0

        return n//5 + self.trailingZeroes(n//5)


    def trailingZeroes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 1
        for x in range(n):
            result *= x+1
        cnt =0;
        for x in reversed(str(result)):
            if x =='0':
                cnt +=1
            else:
                break
        return cnt


if __name__ == '__main__':
    ll = Solution().trailingZeroes(4)
    print(ll)

    print(len('00000000000000000000000000000000000000000000000'))

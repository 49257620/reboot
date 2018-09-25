"""
190. 颠倒二进制位

颠倒给定的 32 位无符号整数的二进制位。

示例:

输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
进阶:
如果多次调用这个函数，你将如何优化你的算法？

"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = bin(n)
        print(x)
        x_str = str(x)[2:]
        result_str = "0b"
        for xx in range(32-len(x_str)):
            x_str ="0"+x_str
        print(x_str)
        for y in reversed(x_str):
            result_str += y
        print(result_str)

        return int(result_str,2)



if __name__ == '__main__':
    ll = Solution().reverseBits(43261596)
    print(ll)



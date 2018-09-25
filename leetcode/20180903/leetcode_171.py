"""
171. Excel表列序号

给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701

"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        base = []
        for x in range(65, 65 + 26):
            base.append(chr(x))

        #print(base)
        lvl = 0
        result = 0;
        for x in reversed(s):

            #result += base.index(x)+1+25*lvl*(base.index(x)+1)
            zz = 26**lvl*(base.index(x)+1)
            print(zz)
            result += zz
            print(result)
            lvl +=1

        return result

if __name__ == '__main__':
    ll = Solution().titleToNumber('AAA')
    print(ll)

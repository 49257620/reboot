"""
168. Excel表列名称

给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"

"""



class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result= ""
        num = n
        base = []
        for x in range(65,65+26):
            base.append(chr(x))

        mid = []
        while True:
            if num == 0: break
            num, rem = divmod(num, 26)
            mid.append(rem)

        for x in range(len(mid)) :
            """
            if mid[x] == 0 and x != (len(mid)-1):
                mid[x+1] = mid[x+1]-1
            print(mid)
            
            if x ==0 and mid[x] == 0:
                if mid[x+1] > 0:
                    mid[x + 1] = mid[x + 1] - 1
                    result = base[mid[x] - 1] + result
                continue
            """
            #print(mid)
            if x != len(mid) -1:
                result = base[mid[x] - 1] + result
                if mid[x] <= 0:
                    mid[x] =  mid[x] -1
                    mid[x + 1] = mid[x + 1] - 1
            else:
                if mid[x] == 0:
                    continue
                else:
                    result = base[mid[x] -1] + result


        return result

if __name__ == '__main__':
    ll = Solution().convertToTitle(701)
    print(ll)
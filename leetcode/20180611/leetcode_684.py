# encoding: utf-8
# Author: LW


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        print([ x for x in edges if x[0]==2 or x[1]==2])
        result = []
        x_list = []
        y_list = []
        for i in range(len(edges)):
            x, y = edges[i][0], edges[i][1]
            result.append(x)
            result.append(y)
            #print(x,y)

        temp = []
        for i in range(1,len(edges)+1):
            print(i,result.count(i))
            if result.count(i)==1:
                temp.extend([ x for x in edges if x[0]==i or x[1]==i])

        for i in temp:
            if i in edges:
                edges.remove(i)

        print(edges)


        return result

"""
[[1,2],[1,3],[2,3]]             -> [2,3]
[[1,2],[1,3],[2,4],[1,4]]       -> [1,4]
[[1,2],[2,3],[3,4],[1,4],[1,5]] -> [1,4]
[[1,5],[3,4],[3,5],[4,5],[2,4]] -> [4,5]
[[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]] - > [8, 10]

[[9, 10], [5, 8], [4, 9], [8, 10], [4, 10], [6, 8]]
"""

a = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
print(Solution().findRedundantConnection(a))

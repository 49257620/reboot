# encoding: utf-8
# Author: LW
"""
该问题运行环境只有在web上才可以，本地缺少ListNode类型

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # return l1.val,l1.next.val,l1.next.next.val
        temp_l1 = []
        while l1 != None:
            temp_l1.append(l1.val)
            l1 = l1.next
        temp_l2 = []
        while l2 != None:
            temp_l2.append(l2.val)
            l2 = l2.next
        # return  temp_l1,temp_l2
        result = list()
        result.extend(list(temp_l1))
        result.extend(list(temp_l2))
        result = sorted(result)
        return result


a = ListNode([1, 2, 4])
b = ListNode([1, 3, 4])
print(Solution().mergeTwoLists(a, b))

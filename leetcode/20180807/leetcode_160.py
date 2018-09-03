"""
160. 相交链表

编写一个程序，找到两个单链表相交的起始节点。



例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
在节点 c1 开始相交。



注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 超过时间限制
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = headA
        B = headB
        while A :
            B = headB
            while B:
                if A.val == B.val:
                    return B
                B = B.next
            A = A.next
        return None

#通过
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = headA
        A_list = []
        B = headB
        B_list = []
        while A :
            A_list.append(A.val)
            A = A.next
        while B :
            B_list.append(B.val)
            B = B.next
        set3 = set(A_list) & set(B_list)
        if set3:
            aaa = [ A_list.index(x) for x in set3]
            result = ListNode(A_list[min(aaa)])
            return result
        else:
            return None
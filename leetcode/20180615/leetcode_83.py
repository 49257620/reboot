# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp_l1 = []
        while head != None:
            temp_l1.append(head.val)
            head = head.next

        temp_set = set(temp_l1)

        result_list = list(temp_set)

        result = sorted(result_list)
        return result


a = 6

print(Solution().deleteDuplicates(a))
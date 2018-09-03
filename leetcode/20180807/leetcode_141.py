"""

给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？

"""


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    ll = Solution().hasCycle([4,1,2,1,2])
    print(ll)
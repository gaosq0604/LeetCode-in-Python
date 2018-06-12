# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p0 = p1 = head
        while p1 and p1.next:
            p0 = p0.next
            p1 = p1.next.next
            if p0 is p1:
                return True
        return False
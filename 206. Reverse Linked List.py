# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return []
        prev = None
        while head.next:
            next = head.next
            head.next = prev
            prev = head
            head = next
        head.next = prev
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ptr = dummy = ListNode(None)
        ptr.next = head
        while ptr and ptr.next:
            while ptr.next and ptr.next.val == val:
                ptr.next = ptr.next.next
            if ptr: ptr = ptr.next
        '''while dummy and dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next'''
        return dummy.next
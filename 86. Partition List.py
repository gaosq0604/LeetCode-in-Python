# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy=dummy1=ListNode(-1)
        dummym=dummy2=ListNode(-1)
        while head:
            if head.val<x:
                dummy1.next=head
                dummy1=dummy1.next
            else:
                dummy2.next=head
                dummy2=dummy2.next
            head=head.next
        dummy2.next=None
        dummy1.next=dummym.next
        return dummy.next
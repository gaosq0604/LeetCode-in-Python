# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyhead=ListNode(0)
        dummyhead.next=head
        head2=dummyhead
        for i in range(n):
            head=head.next
        while head:
            head=head.next
            head2=head2.next
        head2.next=head2.next.next
        return dummyhead.next
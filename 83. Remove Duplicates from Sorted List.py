# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        while head.next:
            if head.val==head.next.val:
                head.next=head.next.next
            else:
                head=head.next
        return dummy.next
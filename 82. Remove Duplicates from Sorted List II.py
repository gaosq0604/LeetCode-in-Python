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
        p=dummy
        while p.next and p.next.next:
            if p.next.val==p.next.next.val:
                val=p.next.val
                while p.next and p.next.val==val:
                    p.next=p.next.next
            else:
                p=p.next
        return dummy.next
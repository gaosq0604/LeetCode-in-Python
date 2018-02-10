# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy=cur=ListNode(-1)
        dummy.next=l=end=head
        r=head.next
        while True:
            for _ in range(k):
                if not end:
                    return dummy.next
                end=end.next
            for _ in range(k-1):
                r.next,l,r=l,r,r.next
            cur.next=l
            cur=head
            head.next=r
            head=r
            if head:
                l,r=r,r.next
            
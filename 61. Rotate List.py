# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k==0:
            return head
        n=1
        tail=head
        while tail.next:
            tail=tail.next
            n+=1
        k=n-k%n
        if k==0 or k==n:
            return head
        newhead=head
        for _ in range(k-1):
            newhead=newhead.next
        head,tail.next,newhead.next=newhead.next,head,None
        return head
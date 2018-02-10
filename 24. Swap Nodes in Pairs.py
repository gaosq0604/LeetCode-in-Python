# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=cur=ListNode(0)
        dummy.next=head
        while cur.next and cur.next.next:
            p1,p2 =cur.next,cur.next.next
            p1.next,p2.next,cur.next=p2.next,p1,p2
            cur=cur.next.next
        return dummy.next
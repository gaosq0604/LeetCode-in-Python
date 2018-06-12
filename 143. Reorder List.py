# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: 
            return head
        pi = pj = head
        while pj.next and pj.next.next:
            pi, pj = pi.next, pj.next.next
        cur = pi.next
        pi.next = None
        node = None
        while cur:
            cur.next, node, cur = node, cur, cur.next
        cur1, cur2 = head, node
        while cur2:
            next1, next2 = cur1.next, cur2.next
            cur1.next, cur2.next = cur2, next1
            cur1, cur2 = next1, next2
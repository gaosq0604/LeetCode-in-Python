# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1 = len2 = 0
        a, b = headA, headB
        while a:
            len1 += 1
            a = a.next
        while b:
            len2 += 1
            b = b.next
        if len2 > len1:
            for _ in range(len2-len1):
                headB = headB.next
        else:
            for _ in range(len1-len2):
                headA = headA.next
        while headA is not headB:
            headA = headA.next
            headB = headB.next
        return headA
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        b=0
        p=ListNode(0)
        c=p
        while ((l1!=None) & (l2!=None)):
            a=l1.val+l2.val+b
            b=0
            if (a>9):
                a-=10
                b=1
            p.val=a
            l1=l1.next
            l2=l2.next
            if ((l1!=None) | (l2!=None) | (b>0)):
                p.next=ListNode(0)
                p=p.next
        while (l1!=None):
            a=l1.val+b
            b=0
            if (a>9):
                a-=10
                b=1
            p.val=a
            l1=l1.next
            if ((l1!=None) | (b>0)):
                p.next=ListNode(0)
                p=p.next
        while (l2!=None):
            a=l2.val+b
            b=0
            if (a>9):
                a-=10
                b=1
            p.val=a
            l2=l2.next
            if ((l2!=None) | (b>0)):
                p.next=ListNode(0)
                p=p.next
        if (b>0):
            p.val=b
        return c
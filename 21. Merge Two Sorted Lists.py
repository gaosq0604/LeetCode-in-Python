# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead=ListNode(0)
        r=dummyhead
        while l1 and l2:
            if l1.val<=l2.val:
                dummyhead.next=l1
                l1=l1.next
            else:
                dummyhead.next=l2
                l2=l2.next
            dummyhead=dummyhead.next
        if l1:
            dummyhead.next=l1
        elif l2:
            dummyhead.next=l2
        return r.next
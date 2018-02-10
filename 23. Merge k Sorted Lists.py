# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        r=[]
        for lst in lists:
            while lst:
                r.append(lst.val)
                lst=lst.next
        return sorted(r)
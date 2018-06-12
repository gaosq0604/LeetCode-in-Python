# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insert_node(self, head, node):
        prev, curr = None, head
        while curr.val < node.val:
            prev, curr = curr, curr.next
        if not prev:
            head = node
        else:
            prev.next = node
        node.next = curr
        return head
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        tail = head
        curr = head.next
        while curr:
            if curr.val < tail.val:
                link = curr.next
                head = self.insert_node(head, curr)
                del curr
                tail.next = curr = link
            else:
                tail = tail.next
                curr = curr.next
        return head
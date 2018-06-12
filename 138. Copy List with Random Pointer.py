# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
			return
        temp = head
        node_map = collections.defaultdict(lambda: RandomListNode(0))
        node_map[None] = None
        while temp:
            node_map[temp].label = temp.label
            node_map[temp].next = node_map[temp.next]
            node_map[temp].random = node_map[temp.random]
            temp = temp.next
        return node_map[head]
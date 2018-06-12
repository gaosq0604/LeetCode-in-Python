# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        self.node = head
        return self.dfs(0, l-1)
    def dfs(self, left, right):
        if left > right:
            return None
        mid = left+(right-left)//2
        l = self.dfs(left, mid-1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next
        r = self.dfs(mid+1, right)
        root.right = r
        return root
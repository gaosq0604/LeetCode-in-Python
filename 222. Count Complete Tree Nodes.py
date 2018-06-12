# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        l, r = self.getDepth(root.left), self.getDepth(root.right)
        if l == r:
            return 2 ** l + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + 2 ** r
        
    def getDepth(self, node):
        if not node: return 0
        depth = 1
        while node.left:
            node = node.left
            depth += 1
        return depth
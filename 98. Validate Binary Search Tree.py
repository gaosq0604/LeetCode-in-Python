# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, floor = float('-inf'), ceiling = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val >= ceiling or root.val <= floor:
            return False
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)
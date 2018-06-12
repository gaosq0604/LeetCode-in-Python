# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return None
        left, right = root.left, root.right
        if left:
            self.flatten(left)
            tail = left
            while tail.right:
                tail = tail.right
            root.left, root.right, tail.right = None, root.left, root.right
        self.flatten(right)
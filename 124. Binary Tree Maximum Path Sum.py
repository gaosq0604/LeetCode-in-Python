# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: return 0
            left, right = max(dfs(node.left), 0), max(dfs(node.right), 0)
            self.res = max(self.res, left + right + node.val)
            return node.val + max(left, right)
            
        self.res = float('-inf')
        dfs(root)
        return self.res
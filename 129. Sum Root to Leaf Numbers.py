# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = 0
        self.dfs(root, 0)
        return self.res
    def dfs(self, root, path):
        path = path*10+root.val
        if not root.left and not root.right:
            self.res += path
        else:
            if root.left:
                self.dfs(root.left, path)
            if root.right:
                self.dfs(root.right, path)
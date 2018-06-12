# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1
    def dfs(self, root):
        if not root:
            return 0
        lh, rh = self.dfs(root.left), self.dfs(root.right)
        if lh == -1 or rh == -1 or abs(lh-rh) > 1:
            return -1
        return max(lh, rh)+1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        self.res = []
        self.sum = sum
        self.dfs(root, root.val, [root.val])
        return self.res
    def dfs(self, root, sums, path):
        if not root.left and not root.right and sums == self.sum:
            self.res.append(path)
        else:
            if root.left:
                self.dfs(root.left, sums+root.left.val, path+[root.left.val])
            if root.right:
                self.dfs(root.right, sums+root.right.val, path+[root.right.val])
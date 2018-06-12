# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack[-1]
            if node.left or node.right:
                if node.right:
                    stack.append(node.right)
                    node.right = None
                if node.left:
                    stack.append(node.left)
                    node.left = None
            else:
                res.append(stack.pop().val)
        return res
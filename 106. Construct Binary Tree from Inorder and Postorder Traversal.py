# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            val = postorder.pop()
            idx = inorder.index(val)
            root = TreeNode(val)
            root.right = self.buildTree(inorder[idx+1:], postorder)
            root.left = self.buildTree(inorder[:idx], postorder)
            return root
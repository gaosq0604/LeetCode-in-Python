# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self,root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.res=[]
        self.inorder(root)
        return self.res
    def inorder(self,root):
        if root.left:
            self.inorder(root.left)
        self.res.append(root.val)
        if root.right:
            self.inorder(root.right)
    
    #return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []
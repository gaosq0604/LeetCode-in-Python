# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.order = []
        self.prev = None
        self.inorder(root)
        self.swap(self.order[0],self.order[-1])
        return    
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        if self.prev and self.prev.val > root.val:
            self.order += [self.prev,root]
        self.prev = root
        self.inorder(root.right)
        return  
    def swap(self, r1, r2):
        r1.val,r2.val = r2.val,r1.val
        return
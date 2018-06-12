# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root and root.left:
            cur = root
            while cur:
                cur.left.next = cur.right
                cur.right.next = cur.next and cur.next.left
                cur = cur.next
            root = root.left
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        while matrix:
            res+=matrix.pop(0)
            matrix=list(zip(*matrix))[::-1]
        return res
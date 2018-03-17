class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        from math import ceil
        for i in range(ceil(m/2)):
            for j in range(m//2):
                matrix[j][-1-i],matrix[-1-i][-1-j],matrix[-1-j][i],matrix[i][j]=matrix[i][j],matrix[j][-1-i],matrix[-1-i][-1-j],matrix[-1-j][i]
        #matrix[:]=list(zip(*matrix[::-1]))
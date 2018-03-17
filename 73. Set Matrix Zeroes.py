class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for t in range(m):
                        if matrix[t][j] and matrix[t][j]!='x':
                            matrix[t][j]='x'
                    for t in range(n):
                        if matrix[i][t] and matrix[i][t]!='x':
                            matrix[i][t]='x'
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='x':
                    matrix[i][j]=0
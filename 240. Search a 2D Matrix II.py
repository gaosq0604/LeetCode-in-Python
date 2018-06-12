class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >= 0 and j <= n-1:
            num = matrix[i][j]
            if target == num:
                return True
            elif target > num:
                j += 1
            else:
                i -= 1
        return False'''
        if not matrix or not matrix[0]:
            return False
        
        def search(startY, startX, maxY, maxX):
            if startY >= maxY or startX >= maxX:
                return False
            
            # marching through diagonal
            y, x = startY, startX
            while y < maxY and x < maxX and matrix[y][x] < target:
                y, x = y + 1, x + 1
            
            # divide and conquer if target is not on this diagonal
            if y < maxY and x < maxX and matrix[y][x] == target:
                return True
            else:
                return search(startY, x, y, maxX) or search(y, startX, maxY, x)
        
        return search(0, 0, len(matrix), len(matrix[0]))
        
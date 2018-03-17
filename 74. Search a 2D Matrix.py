class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m,n=len(matrix),len(matrix[0])
        start,end=0,m*n-1
        while start<=end:
            mid=(start+end)//2
            num=matrix[mid//n][mid%n]
            if num==target: return True
            elif num<target: start=mid+1
            elif num>target: end=mid-1
        return False
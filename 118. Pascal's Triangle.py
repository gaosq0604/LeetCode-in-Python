class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res += [[1] + [res[i-1][j]+res[i-1][j+1] for j in range(i-1)] + [1]]
        return res if numRows else []
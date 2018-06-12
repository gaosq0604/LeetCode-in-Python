class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            res = [1]+[res[j]+res[j+1] for j in range(i)]+[1]
        return res
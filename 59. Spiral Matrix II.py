class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        S,low=[],n*n+1
        while low>1:
            low,high=low-len(S),low
            S=[list(range(low,high))]+list(zip(*S[::-1]))
        return S
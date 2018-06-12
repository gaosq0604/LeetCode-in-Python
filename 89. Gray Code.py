class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[0]
        for i in range(n):
            res+=[x+2**i for x in reversed(res)]
        return res
        #return [(i>>1)^i for i in range(2**n)]
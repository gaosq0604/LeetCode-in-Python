class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=[1]*n
        for _ in range(m-1):
            for i in range(1,n):
                res[i]+=res[i-1]
        return res[-1]
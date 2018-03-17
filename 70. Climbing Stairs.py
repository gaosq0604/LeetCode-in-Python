class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=b=1
        for _ in range(n-1):
            a,b=a+b,a
        return a
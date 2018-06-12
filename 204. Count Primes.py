class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        if n <= 2: return 0
        res = [1] * n
        res[0] = res[1] = 0
        for i in range(2, int(sqrt(n))+1):
            if res[i]:
                res[i*i:n:i] = [0]*len(res[i*i:n:i])
        return sum(res)
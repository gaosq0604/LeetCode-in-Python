class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if not m: return 0
        dp = [triangle[0][0]]+[float('inf')]*(m-1)
        for i in range(1, m):
            for j in range(i, -1, -1):
                if j == 0:
                    dp[j] += triangle[i][j]
                elif j == i:
                    dp[j] = dp[j-1]+triangle[i][-1]
                else:
                    dp[j] = min(dp[j], dp[j-1])+triangle[i][j]
        return min(dp)
        '''dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]'''
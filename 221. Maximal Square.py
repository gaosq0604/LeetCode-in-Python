class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        curmax = 0
        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                if curmax == 0: curmax = 1
        for i in range(1, m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                if curmax == 0: curmax = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    if dp[i][j] > curmax: curmax = dp[i][j]
        return curmax * curmax
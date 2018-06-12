class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[-1][-1] = max(1-dungeon[-1][-1], 1)
        for i in range(m-2, -1, -1):
            dp[i][-1] = max(dp[i+1][-1]-dungeon[i][-1], 1)
        for j in range(n-2, -1, -1):
            dp[-1][j] = max(dp[-1][j+1]-dungeon[-1][j], 1)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-dungeon[i][j], 1)
        return dp[0][0]
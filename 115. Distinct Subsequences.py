class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        l1, l2 = len(s)+1, len(t)+1
        dp = [[0]*l2 for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = 1
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
        return dp[-1][-1]
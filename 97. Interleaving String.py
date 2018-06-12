class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1,l2,l3 = len(s1),len(s2),len(s3)
        if l1+l2 != l3:
            return False
        dp = [[True]*(l2+1) for _ in range(l1+1)]
        for i in range(1,l1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1,l2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1][-1]
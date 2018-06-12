class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]: return 1
        len_ = len(s)
        dp = [i for i in range(len_)]
        dp[0] = 0
        for i in range(1, len_):
            if s[:i+1] == s[:i+1][::-1]:
                dp[i] = 0
            else:
                dp[i] = dp[i-1]+1
                for j in range(i-1):
                    if dp[j]<dp[i] and s[j+1] == s[i] and s[j+1:i+1] == s[j+1:i+1][::-1]:
                        dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]
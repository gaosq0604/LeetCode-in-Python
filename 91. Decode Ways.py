class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n=len(s)
        dp=[1]+[0]*n
        for i in range(n):
            if s[i]!='0':
                dp[i+1]+=dp[i]
            if i>0 and '10'<=s[i-1:i+1]<='26':
                dp[i+1]+=dp[i-1] 
        return dp[-1]
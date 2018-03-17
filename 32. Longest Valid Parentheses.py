class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp,stack=[0]*(len(s)+1),[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                if stack:
                    p=stack.pop()
                    dp[i+1]=dp[p]+i+1-p
        return max(dp)
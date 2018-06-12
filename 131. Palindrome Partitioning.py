class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        len_ = len(s)
        dp = [[] for _ in range(len_)]
        dp[0] = [[s[0]]]
        for i in range(1, len_):
            dp[i] = [wd+[s[i]] for wd in dp[i-1]]
            if s[:i+1] == s[:i+1][::-1]:
                dp[i].append([s[:i+1]])
            for j in range(i-1):
                if s[j+1] == s[i] and s[j+1:i+1] == s[j+1:i+1][::-1]:
                    dp[i].extend([wd+[s[j+1:i+1]] for wd in dp[j]])
        return dp[-1]
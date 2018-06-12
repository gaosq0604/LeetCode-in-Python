class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        len_ = len(s)
        wordDict=set(wordDict)
        dp = [False]*len_
        for i in range(len_):
            if s[:i+1] in wordDict:
                dp[i] = True
            else:
                for j in range(i)[::-1]:
                    if dp[j] and s[j+1:i+1] in wordDict:
                        dp[i] = True
                        break
        return dp[-1]
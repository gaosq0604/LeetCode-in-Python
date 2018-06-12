class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
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
        if dp[-1] == False: return []
        dp = [[] for _ in range(len_)]
        for i in range(len_):
            if s[:i+1] in wordDict:
                dp[i] = [[s[:i+1]]]
            for j in range(i)[::-1]:
                if dp[j] and s[j+1:i+1] in wordDict:
                    dp[i].extend([wd+[s[j+1:i+1]] for wd in dp[j]])
        return [' '.join(s) for s in dp[-1]]
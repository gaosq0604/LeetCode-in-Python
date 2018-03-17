class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        def dfs(remain,stack):
            if remain==0:
                res.append(stack)
                return 
            for item in candidates:
                if item>remain:
                    break
                if not stack or item>=stack[-1]:
                    dfs(remain-item,stack+[item])
        dfs(target,[])
        return res
        '''dp = [[]] + [[] for i in range(target)]
        for i in range(1, target + 1):
            for number in candidates:
                if number > i: break
                for L in dp[i - number]:
                    if not L or number >= L[-1]: dp[i] += L + [number],
        return dp[target]'''
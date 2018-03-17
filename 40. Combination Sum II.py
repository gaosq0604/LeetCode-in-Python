class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        def dfs(remain,start,stack):
            if remain==0:
                res.append(stack)
                return 
            for i in range(start,len(candidates)):
                if candidates[i]>remain:
                    break
                if i!=start and candidates[i]==candidates[i-1]:
                    continue
                if not stack or candidates[i]>=stack[-1]:
                    dfs(remain-candidates[i],i+1,stack+[candidates[i]])
        dfs(target,0,[])
        return res
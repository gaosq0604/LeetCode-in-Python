class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, 10))
        res = []
        def dfs(remain, start, path):
            if remain == 0:
                if len(path) == k:
                    res.append(path)
                else:
                    return
            if len(path) == k: return
            for i in range(start, 9):
                if nums[i] > remain:
                    break
                dfs(remain-nums[i], i+1, path+[nums[i]])
        dfs(n, 0, [])
        return res
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res=[]
        def dfs(left,s,k):
            if k==0:
                self.res.append(s)
                return
            for i in range(len(left)-k+1):
                dfs(left[i+1:],s+[left[i]],k-1)
        dfs(list(range(1,n+1)),[],k)
        return self.res
        '''if k == 1:
            return [[i] for i in range(1, n+1)]
        if n == k:
            return [[i for i in range(1, n+1)]]
        return [i + [n] for i in self.combine(n-1,k-1)] + [i for i in self.combine(n-1, k)]'''
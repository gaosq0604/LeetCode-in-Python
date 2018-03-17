class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res=0
        def dfs(col,sum1,sum2):
            p=len(col)
            if p==n:
                self.res+=1
                return
            for q in range(n):
                if q not in col and p+q not in sum1 and p-q not in sum2:
                    dfs(col+[q],sum1+[p+q],sum2+[p-q])
        dfs([],[],[])
        return self.res
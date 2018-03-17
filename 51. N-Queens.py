class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(col,sum1,sum2):
            p=len(col)
            if p==n:
                res.append(col)
                return
            for q in range(n):
                if q not in col and p+q not in sum1 and p-q not in sum2:
                    dfs(col+[q],sum1+[p+q],sum2+[p-q])
        res=[]
        dfs([],[],[])
        return [['.'*q+'Q'+'.'*(n-q-1) for q in item] for item in res]
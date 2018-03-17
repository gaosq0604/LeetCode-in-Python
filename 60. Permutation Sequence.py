class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from functools import reduce
        array=list(range(1,n+1))
        divide=reduce(lambda x,y:x*y,range(1,n)) if n>1 else 1
        k-=1
        res=[]
        for i in range(n-1,0,-1):
            res.append(array.pop(k//divide))
            k%=divide
            divide//=i
        res+=array
        return ''.join(map(str,res))
            
            
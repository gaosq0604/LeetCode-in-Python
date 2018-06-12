class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res=[]
        self.dfs(s,4,[])
        return ['.'.join(x) for x in self.res]
    
    def dfs(self,s,k,path):
        if len(s)>k*3:
            return
        if k==0:
            self.res.append(path)
        else:
            for i in range(min(3,len(s)-k+1)):
                if i==2 and int(s[:3])>255 or i>0 and s[0]=='0':
                    continue
                self.dfs(s[i+1:],k-1,path+[s[:i+1]])
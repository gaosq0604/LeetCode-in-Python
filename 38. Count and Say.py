class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s='1'
        for _ in range(n-1):
            count=1
            temp=''
            for idx in range(1,len(s)):
                if s[idx]==s[idx-1]:
                    count+=1
                else:
                    temp+=str(count)+s[idx-1]
                    count=1
            temp+=str(count)+s[-1]
            s=temp
        return s
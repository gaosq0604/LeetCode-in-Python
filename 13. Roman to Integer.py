class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        r=0
        for i in range(0,len(s)-1):
            if d[s[i]]<d[s[i+1]]:
                r-=d[s[i]]
            else:
                r+=d[s[i]]
        return r+d[s[-1]]
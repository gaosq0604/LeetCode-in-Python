class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i=l=r=0
        need,miss=collections.Counter(t),len(t)
        for j,ch in enumerate(s,1):
            miss-=need[ch]>0
            need[ch]-=1
            if miss<=0:
                while i<j and need[s[i]]<0:
                    need[s[i]]+=1
                    i+=1
                if not r or j-i<r-l:
                    l,r=i,j
        return s[l:r]
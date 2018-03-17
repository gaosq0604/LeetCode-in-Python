class Solution:
    cache={}
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''if (s,p) in self.cache:
            return self.cache[(s,p)]
        if not p:
            return not s
        if len(p)-p.count('*')>len(s):
            self.cache[(s,p)]=False
            return False
        if p[-1]=='*':
            if self.isMatch(s,p[:-1]):
                self.cache[(s,p[:-1])]=True
                return True
            if s and self.isMatch(s[:-1],p):
                self.cache[(s[:-1],p)]=True
                return True
        if s and (s[-1]==p[-1] or p[-1]=='?'):
            if s and self.isMatch(s[:-1],p[:-1]):
                self.cache[(s[:-1],p[:-1])]=True
                return True
        self.cache[(s,p)]=False
        return False'''
        if not p:
            return not s
        m, n = len(s), len(p)
        i = j = 0
        last_x = 0
        last_y = -1
        while i < m:
            if j < n and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                last_x = i
                last_y = j
                j += 1
            elif last_y >= 0:
                last_x += 1
                i = last_x
                j = last_y
            else:
                return False
        while j < n and p[j] == '*':
            j += 1
        return j == n
            
        
class Solution:
    cache = {}
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''if p=='':
            return s==''
        if s=='':
            if len(p)%2==1:
                return False
            i=1
            while i<len(p):
                if p[i]!='*':
                    return False
                i+=2
            return True
        if len(p)>1 and p[1]=='*':
            if p[0]=='.' or p[0]==s[0]:
                return self.isMatch(s,p[2:]) or self.isMatch(s[1:],p)
            else:
                return self.isMatch(s,p[2:])
        elif p[0]=='.' or p[0]==s[0]:
            return self.isMatch(s[1:],p[1:])
        else:
            return False'''
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            return not s
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False
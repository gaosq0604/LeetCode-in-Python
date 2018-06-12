class Solution:
    d={}
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1,s2) in self.d:
            return self.d[(s1,s2)]
        if len(s1)!=len(s2) or sorted(s1)!=sorted(s2):
            return False
        if s1==s2:
            return True
        for i in range(1,len(s1)):
            if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])) or \
                (self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i])):
                self.d[(s1,s2)]=True
                return True
        self.d[(s1,s2)]=False
        return False

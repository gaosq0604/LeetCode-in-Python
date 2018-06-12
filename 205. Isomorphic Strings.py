class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return len(d.values()) == len(set(d.values()))
        # return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        # return [s.find(i) for i in s] == [t.find(j) for j in t]
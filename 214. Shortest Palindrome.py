class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        k = 0
        r = s[::-1]
        for i in range(m):
            # if r[i:] == s[:m-i]:
            if s.startswith(r[i:]):
                k = i
                break
        return r[:k] + s
        '''for i in range(m)[::-1]:
            if s[i] == s[0] and s[:i+1] == s[:i+1][::-1]:
                    k = i
                    break
        return s[k+1:][::-1] + s'''
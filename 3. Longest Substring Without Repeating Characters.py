class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0
        p=''
        for i in range(len(s)):
            if s[i] not in p:
                p+=s[i]
                if len(p)>a:
                    a=len(p)
            else:
                q=p.find(s[i])
                p=p[q+1:len(p)]
                p+=s[i]
        return a
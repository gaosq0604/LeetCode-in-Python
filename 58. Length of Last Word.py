class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.rstrip()
        return len(s.split(' ')[-1])
        #return s[::-1].find(' ')>0 and s[::-1].find(' ') or len(s)
        #return s[::-1].find(' ') if s[::-1].find(' ')>0 else len(s)
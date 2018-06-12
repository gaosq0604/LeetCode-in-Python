class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''res = 0
        base = 1
        for ch in s[::-1]:
            res += (ord(ch)-ord('A')+1)*base
            base *= 26
        return res'''
        return sum((ord(ch) - 64) * (26 ** exp) for exp, ch in enumerate(s[::-1]))
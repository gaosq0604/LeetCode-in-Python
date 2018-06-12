class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = [ch for ch in s.lower() if ch.isalnum()]
        return res == res[::-1]
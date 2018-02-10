class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l=len(haystack)
        k=len(needle)
        for i in range(l-k+1):
            if haystack[i:i+k]==needle:
                return i
        return -1